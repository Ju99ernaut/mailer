import data

from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Path, Query, status
from models import Email, Message

router = APIRouter(prefix="/subscribers", tags=["subscribers"])


@router.get("", response_model=List[Email])
async def read_subcribers(
    page: Optional[int] = Query(0, minimum=0, description="Page number"),
    size: Optional[int] = Query(50, maximum=100, description="Page size"),
):
    return [sub for sub in data.get_all_emails(page, size)]


@router.get("/blocked", response_model=List[Email])
async def read_blocked_subscribers(
    page: Optional[int] = Query(0, minimum=0, description="Page number"),
    size: Optional[int] = Query(50, maximum=100, description="Page size"),
):
    return [sub for sub in data.get_blocked_subscribers(page, size)]


@router.get("/{id}", response_model=Email)
async def read_subscriber_with_id(id: int = Path(..., description="Subscriber ID")):
    subscriber = data.get_subscriber(id)
    if not subscriber:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Template not found"
        )
    return subscriber


@router.get("/{id}/block", response_model=Message)
async def block_subscriber_with_id(id: int = Path(..., description="Subscriber ID")):
    data.block_subscriber(id)
    return {"msg": "success"}


@router.delete("/{id}", response_model=Message)
async def delete_subscriber_with_id(id: int = Path(..., description="Subscriber ID")):
    data.remove_subscriber(id)
    if data.get_subscriber(id):
        raise HTTPException(
            status_code=status.HTTP_417_EXPECTATION_FAILED,
            detail="Failed to unregister",
        )
    return {"msg": "success"}
