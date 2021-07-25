import os
from datetime import datetime

from constants import *

from utils.db import connect_db
import config


@connect_db
def add_user(db, username, email, password):
    table = db[USERS_TABLE]
    activate = True
    if (os.getenv("MAIL_USERNAME") and os.getenv("MAIL_PASSWORD")) or (
        config.CONFIG.mail_username and config.CONFIG.mail_password
    ):
        activate = False
    table.insert(
        {
            USERNAME_KEY: username,
            EMAIL_KEY: email,
            PASSWORD_KEY: password,
            JOINED_KEY: datetime.utcnow(),
            ACTIVE_KEY: activate,
            ROLE_KEY: "user",
        },
    )


@connect_db
def update_user(db, user_id, data):
    table = db[USERS_TABLE]
    table.update(
        {"id": user_id, **{k: v for k, v in data.dict().items() if v is not None}},
        ["id"],
    )


@connect_db
def activate_user(db, user_id, data):
    table = db[USERS_TABLE]
    table.update(
        {"id": user_id, **data},
        ["id"],
    )


@connect_db
def remove_user(db, username, email, password):
    table_users = db[USERS_TABLE]
    table_apps = db[APPS_TABLE]
    table_ratings = db[RATINGS_TABLE]
    # table_docs = db[DOCS_TABLE]
    deleted = table_users.find_one(username=username)
    table_users.delete(username=username, email=email, password=password)
    table_apps.delete(owner=deleted["id"])
    table_ratings.delete(user=deleted["id"])
    # table_docs.delete(application=app_id)


@connect_db
def get_user(db, username):
    table = db[USERS_TABLE]
    row = table.find_one(username=username)
    if row is not None:
        return row
    return None


@connect_db
def get_user_by_id(db, user_id):
    table = db[USERS_TABLE]
    row = table.find_one(id=user_id)
    if row is not None:
        return row
    return None


@connect_db
def get_user_by_email(db, email):
    table = db[USERS_TABLE]
    row = table.find_one(email=email)
    if row is not None:
        return row
    return None
