import data.emails as data

from uuid import UUID
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


@router.get("/blacklisted", response_model=List[Email])
async def read_blacklisted_subscribers(
    page: Optional[int] = Query(0, minimum=0, description="Page number"),
    size: Optional[int] = Query(50, maximum=100, description="Page size"),
):
    return [sub for sub in data.get_blocked_subscribers(page, size)]


@router.get("/{uuid}", response_model=Email)
async def read_subscriber_with_id(
    uuid: UUID = Path(..., description="Subscriber UUID")
):
    subscriber = data.get_subscriber(uuid)
    if not subscriber:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Subscriber not found"
        )
    return subscriber


@router.delete("/{uuid}", response_model=Message)
async def delete_subscriber_with_id(
    uuid: UUID = Path(..., description="Subscriber ID")
):
    data.remove_subscriber(uuid)
    if data.get_subscriber(uuid):
        raise HTTPException(
            status_code=status.HTTP_417_EXPECTATION_FAILED,
            detail="Failed to remove subscriber",
        )
    return {"msg": "success"}
