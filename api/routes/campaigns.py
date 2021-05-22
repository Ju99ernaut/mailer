import data

from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Path, Query, status
from models import Message, Newsletter, Campaign, CampaignConfig
from mail.send import newsletter
from constants import EMAIL_KEY

router = APIRouter(prefix="/campaigns", tags=["campaigns"])


@router.post("/setup", response_model=Message)
async def add_settings_and_credentials_for_newsletter(campaign: CampaignConfig):
    data.add_campaign_config(campaign.dict())
    return {"msg": "success"}


@router.get("/setups", response_model=List[CampaignConfig])
async def read_settings_and_credentials_for_newsletter(
    page: Optional[int] = Query(0, minimum=0, description="Page number"),
    size: Optional[int] = Query(50, maximum=100, description="Page size"),
):
    return [config for config in data.get_all_configs(page, size)]


@router.get("/setups/{id}", response_model=CampaignConfig)
async def read_settings_and_credentials_for_newsletter_with_id(
    id: int = Path(..., description="Config ID")
):
    config = data.get_config(id)
    if not config:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Config not found"
        )
    return config


@router.delete("/setups/{id}", response_model=CampaignConfig)
async def delete_settings_and_credentials_for_newsletter(
    id: int = Path(..., description="Config ID")
):
    config = data.remove_config(id)
    if data.get_config(id):
        raise HTTPException(
            status_code=status.HTTP_417_EXPECTATION_FAILED, detail="Config not deleted"
        )
    return config


@router.post("/post", response_model=Message)
async def post_newsletter_to_mailing_list(post: Newsletter):
    mail_list = list(map(lambda row: row[EMAIL_KEY], data.get_all_emails()))
    await newsletter(mail_list, post.subject, post.body)
    return {"msg": "success"}


@router.get("", response_model=List[Campaign])
async def get_all_campaigns(
    page: Optional[int] = Query(0, minimum=0, description="Page number"),
    size: Optional[int] = Query(50, maximum=100, description="Page size"),
):
    return [campaign for campaign in data.get_campaigns(page, size)]


@router.get("/{id}", response_model=Campaign)
async def get_campaign_with_id(id: int = Path(..., description="Campaign ID")):
    campaign = data.get_campaign(id)
    if not campaign:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Campaign not found"
        )
    return campaign