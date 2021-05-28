from constants import *

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
def get_all_templates(db, offset, limit):
    table = db[TEMPLATES_TABLE]
    return table.find()


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
def get_blocked_subscribers(db, offset, limit):
    table = db[EMAILS_TABLE]
    return table.find(status="blacklisted")


@connect_db
def remove_subscriber(db, uuid):
    table = db[EMAILS_TABLE]
    table.delete(uuid=str(uuid))


@connect_db
def get_subscriber(db, uuid):
    table = db[EMAILS_TABLE]
    row = table.find_one(uuid=str(uuid))
    if row is not None:
        return row
    return None


@connect_db
def get_all_emails(db, offset, limit):
    table = db[EMAILS_TABLE]
    return table.find()


@connect_db
def add_uppy_config(db, config):
    table = db[UPPY_TABLE]
    config["id"] = 1
    table.upsert(config, ["id"])


@connect_db
def get_uppy_config(db):
    table = db[UPPY_TABLE]
    row = table.find_one(id=1)
    if row is not None:
        return row
    return None


@connect_db
def add_asset(db, asset):
    table = db[ASSETS_TABLE]
    asset[UUID_KEY] = str(asset[UUID_KEY])
    table.upsert(asset, [UUID_KEY])


@connect_db
def remove_asset(db, uuid):
    table = db[ASSETS_TABLE]
    table.delete(uuid=str(uuid))


@connect_db
def get_asset(db, uuid):
    table = db[ASSETS_TABLE]
    row = table.find_one(uuid=str(uuid))
    if row is not None:
        return row
    return None


@connect_db
def get_all_assets(db, offset, limit):
    table = db[ASSETS_TABLE]
    return table.find()


@connect_db
def add_campaign(db, campaign):
    table = db[CAMPAIGNS_TABLE]
    campaign[UUID_KEY] = str(campaign[UUID_KEY])
    campaign[TEMPLATE_KEY] = str(campaign[TEMPLATE_KEY])
    table.upsert(campaign, [UUID_KEY])


@connect_db
def get_campaign(db, uuid):
    table = db[CAMPAIGNS_TABLE]
    row = table.find_one(uuid=str(uuid))
    if row is not None:
        return row
    return None


@connect_db
def get_all_campaigns(db, offset, limit):
    table = db[CAMPAIGNS_TABLE]
    return table.find()


@connect_db
def add_campaign_config(db, config):
    table = db[CONFIG_TABLE]
    config[UUID_KEY] = str(config[UUID_KEY])
    table.upsert(config, [UUID_KEY])


@connect_db
def remove_campaign_config(db, uuid):
    table = db[CONFIG_TABLE]
    table.delete(uuid=str(uuid))


@connect_db
def get_campaign_config(db, uuid):
    table = db[CONFIG_TABLE]
    row = table.find_one(uuid=str(uuid))
    if row is not None:
        return row
    return None


@connect_db
def get_campaign_config_default(db):
    table = db[CONFIG_TABLE]
    row = table.find_one(id=id)
    if row is not None:
        return row
    return None


@connect_db
def get_all_campaign_configs(db, offset, limit):
    table = db[CONFIG_TABLE]
    return table.find()
