from constants import (
    USERS_TABLE,
    USERNAME_KEY,
    ROLE_KEY,
    EMAIL_KEY,
)

from utils.db import connect_db


@connect_db
def admin_get_user(db, user_id):
    table = db[USERS_TABLE]
    row = table.find_one(id=user_id)
    if row is not None:
        return row
    return None


@connect_db
def admin_get_users(db):
    table = db[USERS_TABLE]
    all_items = table.all()
    return all_items


@connect_db
def admin_set_username_role(db, username, role):
    table = db[USERS_TABLE]
    table.update(
        {USERNAME_KEY: username, ROLE_KEY: role},
        [USERNAME_KEY],
    )


@connect_db
def admin_set_email_role(db, email, role):
    table = db[USERS_TABLE]
    table.update(
        {EMAIL_KEY: email, ROLE_KEY: role},
        [EMAIL_KEY],
    )


@connect_db
def admin_remove_user(db, user_id):
    table_users = db[USERS_TABLE]
    table_users.delete(id=user_id)
