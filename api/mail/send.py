import data

from typing import List
from pydantic import EmailStr
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

# from fastapi_mail.email_utils import DefaultChecker

current_config = data.get_campaign_config() or {
    "MAIL_USERNAME": "",
    "MAIL_PASSWORD": "",
    "MAIL_FROM": "user@example.com",
    "MAIL_PORT": 587,
    "MAIL_SERVER": "smtp.gmail.com",
    "MAIL_FROM_NAME": "Newsletter",
    "MAIL_TLS": True,
    "MAIL_SSL": False,
    "USE_CREDENTIALS": True,
}

conf = ConnectionConfig(
    MAIL_USERNAME=current_config["MAIL_USERNAME"] or "",
    MAIL_PASSWORD=current_config["MAIL_PASSWORD"] or "",
    MAIL_FROM=current_config["MAIL_FROM"] or "user@example.com",
    MAIL_PORT=current_config["MAIL_PORT"],
    MAIL_SERVER=current_config["MAIL_SERVER"],
    MAIL_FROM_NAME=current_config["MAIL_FROM_NAME"],
    MAIL_TLS=current_config["MAIL_TLS"],
    MAIL_SSL=current_config["MAIL_SSL"],
    USE_CREDENTIALS=current_config["USE_CREDENTIALS"],
    TEMPLATE_FOLDER="./api/templates",
)


async def newsletter(to: List[EmailStr], subject: str, body: str):
    message = MessageSchema(
        subject=subject,
        recipients=to,
        body=body,
        subtype="html",
    )
    if current_config["MAIL_USERNAME"] and current_config["MAIL_PASSWORD"]:
        fm = FastMail(conf)
        await fm.send_message(message)


async def use_template(to: List[EmailStr], subject: str, body: dict, template: str):
    message = MessageSchema(
        subject=subject,
        recipients=to,
        body=body,
        subtype="html",
    )
    if current_config["MAIL_USERNAME"] and current_config["MAIL_PASSWORD"]:
        fm = FastMail(conf)
        await fm.send_message(message, template=template)
