from typing import Optional
from uuid import UUID, uuid4
from fastapi import Query
from pydantic import BaseModel, Field, EmailStr

import config

config.parse_args()


class Template(BaseModel):
    id: Optional[str] = ""
    idx: UUID = Field(default_factory=uuid4)
    thumbnail: Optional[str] = ""
    template: Optional[bool] = False
    assets: Optional[str] = Query("", alias=f"{config.CONFIG.prefix}assets")
    html: Optional[str] = Query("", alias=f"{config.CONFIG.prefix}html")
    css: Optional[str] = Query("", alias=f"{config.CONFIG.prefix}css")
    components: Optional[str] = Query("", alias=f"{config.CONFIG.prefix}components")
    styles: Optional[str] = Query("", alias=f"{config.CONFIG.prefix}styles")


class Newsletter(BaseModel):
    subject: Optional[str] = "Newsletter"
    html: str


class Email(BaseModel):
    email: EmailStr


class Message(BaseModel):
    msg: Optional[str] = "success"


class Asset(BaseModel):
    id: Optional[int] = None
    url: str
