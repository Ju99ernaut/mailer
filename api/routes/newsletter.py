import data

from typing import List

from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import EmailStr
from models import Email, Message, Newsletter
from mail.send import newsletter
from constants import EMAIL_KEY

router = APIRouter(prefix="/newsletter", tags=["newsletter"])


@router.post("/register", response_model=Message)
async def register_to_newsletter(email: Email):
    data.add_email(email.email)
    return {"msg": "success"}


@router.get("/register", response_model=Message)
async def register_to_newsletter_querystring(
    email: EmailStr = Query(..., description="Email to register")
):
    data.add_email(email)
    return {"msg": "success"}


@router.get("/unregister", response_model=Message)
async def unregister_to_newsletter(email: Email):
    data.remove_email(email.email)
    if data.get_email(email.email):
        raise HTTPException(
            status_code=status.HTTP_417_EXPECTATION_FAILED,
            detail="Failed to unregister",
        )
    return {"msg": "success"}


@router.get("/unregister", response_model=Message)
async def unregister_to_newsletter_querystring(
    email: EmailStr = Query(..., description="Email to unregister")
):
    data.remove_email(email)
    if data.get_email(email):
        raise HTTPException(
            status_code=status.HTTP_417_EXPECTATION_FAILED,
            detail="Failed to unregister",
        )
    return {"msg": "success"}


@router.post("/post", response_model=Message)
async def post_newsletter_to_mailing_list(post: Newsletter):
    mail_list = list(map(lambda row: row[EMAIL_KEY], data.get_all_emails()))
    await newsletter(mail_list, post.subject, post.body)
    return {"msg": "success"}
