import data

from typing import List, Optional

from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Path, Query, status
from models import Asset, UppyConfig, Message

router = APIRouter(
    prefix="/assets",
    tags=["assets"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[Asset])
async def read_assets(
    page: Optional[int] = Query(0, minimum=0, description="Page number"),
    size: Optional[int] = Query(50, maximum=100, description="Page size"),
):
    return [asset for asset in data.get_all_assets(page, size)]


@router.get("/uppy", response_model=UppyConfig)
async def get_uppy_config():
    uppy_config = data.get_uppy_config()
    if not uppy_config:
        return {"companion_url": "", "endpoint": ""}
    return uppy_config


@router.get("/{uuid}", response_model=Asset)
async def read_asset_with_uuid(uuid: UUID = Path(..., description="Asset UUID")):
    asset = data.get_asset(uuid)
    if not asset:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Asset not found"
        )
    return asset


@router.post("", response_model=Asset)
async def add_asset(asset: Asset):
    data.add_asset(asset.dict())
    return asset


@router.post("/uppy", response_model=UppyConfig)
async def add_uppy_config(uppy_config: UppyConfig):
    data.add_uppy_config(uppy_config.dict())
    return uppy_config


@router.delete(
    "/{uuid}",
    response_model=Message,
)
async def delete_asset_with_idx(uuid: UUID = Path(..., description="Asset UUID")):
    data.remove_asset(uuid)
    return {"msg": "success"}
