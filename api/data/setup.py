import os
from datetime import datetime

from constants import *

from utils.db import connect_db
from utils.password import get_hash

"""Functions for managing a dataset SQL database
    # Schemas

    #################### users ############################
    username: str
    email: str
    password: str
    joined: datetime
    active: bool
    role: str
    
    #################### templates ######################
    id: int
    idx: str
    assets: str
    template: str
    thumbnail: str
    html: str
    css: str
    components: str
    styles: str
    
    #################### emails ######################
    id: int
    email: str

"""


@connect_db
def admin(db):
    username = os.getenv("ADMIN_USERNAME")
    password = os.getenv("ADMIN_PASSWORD")
    email = os.getenv("ADMIN_EMAIL")

    if username and password and email:
        table = db[USERS_TABLE]
        table.upsert(
            {
                USERNAME_KEY: username,
                EMAIL_KEY: email,
                PASSWORD_KEY: get_hash(password),
                JOINED_KEY: datetime.utcnow(),
                ACTIVE_KEY: True,
                ROLE_KEY: "admin",
            },
            [USERNAME_KEY, EMAIL_KEY],
        )


@connect_db
def migrate(db):
    users_table = db[USERS_TABLE]
    users_table.create_column(USERNAME_KEY, db.types.string, unique=True, nullable=False)
    users_table.create_column(EMAIL_KEY, db.types.string, unique=True, nullable=False)

    emails_table = db[EMAILS_TABLE]
    emails_table.create_column(EMAIL_KEY, db.types.string, unique=True, nullable=False)
    db.create_table(TEMPLATES_TABLE, primary_id=IDX_KEY, primary_type=db.types.string)
