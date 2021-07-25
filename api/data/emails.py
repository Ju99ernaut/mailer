from constants import *

from utils.db import connect_db


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
def get_all_emails_unpaginated(db):
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
def get_all_campaigns_unpaginated(db):
    table = db[CAMPAIGNS_TABLE]
    return table.find()


@connect_db
def get_campaign_count(db):
    return len(db[CAMPAIGNS_TABLE])


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
