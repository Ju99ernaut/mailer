import data

from typing import List
from pydantic import EmailStr
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

# from fastapi_mail.email_utils import DefaultChecker


def get_config():
    current_config = data.get_campaign_config_default()
    if not current_config:
        return False
    return ConnectionConfig(
        MAIL_USERNAME=current_config["MAIL_USERNAME"],
        MAIL_PASSWORD=current_config["MAIL_PASSWORD"],
        MAIL_FROM=current_config["MAIL_FROM"],
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
    conf = get_config()
    if conf:
        fm = FastMail(conf)
        await fm.send_message(message)


async def use_template(to: List[EmailStr], subject: str, body: dict, template: str):
    message = MessageSchema(
        subject=subject,
        recipients=to,
        body=body,
        subtype="html",
    )
    conf = get_config()
    if conf:
        fm = FastMail(conf)
        await fm.send_message(message, template=template)
