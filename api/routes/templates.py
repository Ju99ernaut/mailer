import data

from typing import List

from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Path, status
from models import Template
from utils.tasks import prefix

import config

router = APIRouter(
    prefix="/templates",
    tags=["templates"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[Template])
async def read_templates():
    return [
        prefix(config.CONFIG.prefix, template) for template in data.get_all_templates()
    ]


@router.get("/{idx}", response_model=Template)
async def read_template_with_idx(idx: UUID = Path(..., description="Template UUID")):
    template = data.get_template(idx)
    if not template:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Template not found"
        )
    return prefix(config.CONFIG.prefix, template)


@router.post("/{idx}", response_model=Template)
async def add_template(
    template: Template, idx: UUID = Path(..., description="Template UUID")
):
    data.add_template(template.dict())
    template = data.get_template(idx)
    if not template:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Template not found"
        )
    return prefix(config.CONFIG.prefix, template)


@router.delete(
    "/{idx}",
    response_model=List[Template],
)
async def delete_template_with_idx(idx: UUID = Path(..., description="Template UUID")):
    data.remove_template(idx)
    return [
        prefix(config.CONFIG.prefix, template) for template in data.get_all_templates()
    ]
