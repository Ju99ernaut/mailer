from constants import EMAILS_TABLE, TEMPLATES_TABLE, IDX_KEY

from utils.db import connect_db

"""Functions for managing a dataset SQL database
    # Schemas

    #################### templates ######################
    id
    idx
    assets
    template
    thumbnail
    html
    css
    components
    styles
    
    #################### emails ######################
    id
    email

"""


@connect_db
def setup(db):
    emails_table = db[EMAILS_TABLE]

    emails_table.create_column(EMAIL_KEY, db.types.text, unique=True, nullable=False)
    db.create_table(TEMPLATES_TABLE, primary_id=IDX_KEY, primary_type=db.types.text)


@connect_db
def add_template(db, template):
    table = db[TEMPLATES_TABLE]
    template[IDX_KEY] = str(template[IDX_KEY])
    table.upsert(template, [IDX_KEY])


@connect_db
def remove_template(db, idx):
    table = db[TEMPLATES_TABLE]
    table.delete(idx=str(idx))


@connect_db
def get_template(db, idx):
    table = db[TEMPLATES_TABLE]
    row = table.find_one(idx=str(idx))
    if row is not None:
        return row
    return None


@connect_db
def get_all_templates(db):
    table = db[TEMPLATES_TABLE]
    return table.all()


@connect_db
def add_email(db, email):
    table = db[EMAILS_TABLE]
    table.upsert(email, [EMAIL_KEY])


@connect_db
def remove_email(db, email):
    table = db[EMAILS_TABLE]
    table.delete(email=email)


@connect_db
def get_email(db, email):
    table = db[EMAILS_TABLE]
    row = table.find_one(email=email)
    if row is not None:
        return row
    return None


@connect_db
def get_all_emails(db):
    table = db[EMAILS_TABLE]
    return table.all()
