import sys

from datetime import datetime
from constants import *
from utils.db import connect_db
from utils.password import get_hash

import config

config.parse_args()


@connect_db
def add_admin_user(db):
    table = db[USERS_TABLE]
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    table.insert(
        {
            USERNAME_KEY: username,
            EMAIL_KEY: email,
            PASSWORD_KEY: get_hash(password),
            JOINED_KEY: datetime.utcnow(),
            ACTIVE_KEY: True,
            ROLE_KEY: "admin",
        },
    )


if __name__ == "__main__":
    globals()[sys.argv[1]]()
