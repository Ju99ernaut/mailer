from enum import Enum
from typing import List, Optional, Union
from uuid import UUID, uuid4
from datetime import datetime
from fastapi import Query
from pydantic import BaseModel, Field, EmailStr, AnyHttpUrl
from pydantic.class_validators import validator

import config

config.parse_args()


class Template(BaseModel):
    id: Optional[str] = ""
    idx: UUID = Field(default_factory=uuid4)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    thumbnail: Optional[str] = ""
    template: Optional[bool] = False
    assets: Optional[str] = Query("", alias=f"{config.CONFIG.prefix}assets")
    html: Optional[str] = Query("", alias=f"{config.CONFIG.prefix}html")
    css: Optional[str] = Query("", alias=f"{config.CONFIG.prefix}css")
    components: Optional[str] = Query("", alias=f"{config.CONFIG.prefix}components")
    styles: Optional[str] = Query("", alias=f"{config.CONFIG.prefix}styles")


class Newsletter(BaseModel):
    subject: Optional[str] = "Newsletter"
    body: str
    template: UUID = Field(default_factory=uuid4)


class Status(str, Enum):
    enabled = "enabled"
    disabled = "disabled"
    blacklisted = "blacklisted"


class Email(BaseModel):
    id: Optional[int] = None
    uuid: UUID = Field(default_factory=uuid4)
    subscribed_at: datetime = Field(default_factory=datetime.utcnow)
    email: EmailStr
    status: Optional[Status] = "enabled"


class Message(BaseModel):
    msg: Optional[str] = "success"


class Asset(BaseModel):
    id: Optional[int] = None
    uuid: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    type: Optional[str] = None
    filename: Optional[str] = None
    src: AnyHttpUrl
    width: Optional[int] = None
    height: Optional[int] = None


class Campaign(BaseModel):
    uuid: UUID = Field(default_factory=uuid4)
    sent_at: datetime = Field(default_factory=datetime.utcnow)
    subject: str
    body: str
    template: UUID = Field(default_factory=uuid4)
    sent_to: Union[List[EmailStr], str]

    @validator("sent_to")
    def stringify(cls, v):
        if type(v) == list:
            return ",".join(v)
        return v


class CampaignRef(BaseModel):
    id: Optional[int] = None
    uuid: UUID = Field(default_factory=uuid4)
    sent_at: datetime = Field(default_factory=datetime.utcnow)
    subject: str
    body: str
    template: UUID = Field(default_factory=uuid4)
    sent_to: Union[List[EmailStr], str]

    @validator("sent_to")
    def listify(cls, v):
        if type(v) == str:
            return v.split(",")
        return v


class CampaignConfig(BaseModel):
    id: Optional[int] = None
    uuid: UUID = Field(default_factory=uuid4)
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: EmailStr
    MAIL_PORT: Optional[int] = 587
    MAIL_FROM_NAME: Optional[str] = "Newsletter"
    MAIL_SERVER: Optional[str] = "smtp.gmail.com"
    MAIL_TLS: Optional[bool] = True
    MAIL_SSL: Optional[bool] = False
    USE_CREDENTIALS: Optional[bool] = True


class UppyConfig(BaseModel):
    id: Optional[int] = None
    companion_url: Optional[AnyHttpUrl] = None
    endpoint: Optional[AnyHttpUrl] = None
