import data

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import EmailStr
from models import Email, Message

router = APIRouter(prefix="/newsletter", tags=["newsletter"])


@router.post("/subscribe", response_model=Message)
async def subscribe_to_newsletter(email: Email):
    data.add_email(email.dict())
    return {"msg": "success"}


@router.get("/subscribe", response_model=Message)
async def subscribe_to_newsletter_using_querystring(
    email: EmailStr = Query(..., description="Email to register")
):
    data.add_email(Email(email=email).dict())
    return {"msg": "success"}


@router.post("/unsubscribe", response_model=Message)
async def unsubscribe_to_newsletter(email: Email):
    data.remove_email(email.email)
    if data.get_email(email.email):
        raise HTTPException(
            status_code=status.HTTP_417_EXPECTATION_FAILED,
            detail="Failed to unregister",
        )
    return {"msg": "success"}


@router.get("/unsubscribe", response_model=Message)
async def unregister_to_newsletter__using_querystring(
    email: EmailStr = Query(..., description="Email to unregister")
):
    data.remove_email(email)
    if data.get_email(email):
        raise HTTPException(
            status_code=status.HTTP_417_EXPECTATION_FAILED,
            detail="Failed to unregister",
        )
    return {"msg": "success"}
