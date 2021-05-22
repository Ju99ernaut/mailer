import os

from typing import List
from pydantic import EmailStr
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

# from fastapi_mail.email_utils import DefaultChecker

import config

config.parse_args()


conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME") or config.CONFIG.mail_username,
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD") or config.CONFIG.mail_password,
    MAIL_FROM=os.getenv("MAIL_USERNAME")
    or config.CONFIG.mail_username
    or "user@example.com",
    MAIL_PORT=int(config.CONFIG.mail_port),
    MAIL_SERVER=config.CONFIG.mail_server,
    MAIL_FROM_NAME=config.CONFIG.mail_from,
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    TEMPLATE_FOLDER="./api/templates",
)


async def newsletter(to: List[EmailStr], subject: str, body: str):
    message = MessageSchema(
        subject=subject,
        recipients=to,
        body=body,
        subtype="html",
    )
    if (os.getenv("MAIL_USERNAME") and os.getenv("MAIL_PASSWORD")) or (
        config.CONFIG.mail_username and config.CONFIG.mail_password
    ):
        fm = FastMail(conf)
        await fm.send_message(message)


async def use_template(to: List[EmailStr], subject: str, body: dict, template: str):
    message = MessageSchema(
        subject=subject,
        recipients=to,
        body=body,
        subtype="html",
    )
    if (os.getenv("MAIL_USERNAME") and os.getenv("MAIL_PASSWORD")) or (
        config.CONFIG.mail_username and config.CONFIG.mail_password
    ):
        fm = FastMail(conf)
        await fm.send_message(message, template=template)
