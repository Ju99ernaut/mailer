from constants import *

from utils.db import connect_db


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
def get_default_template(db):
    table = db[TEMPLATES_TABLE]
    row = table.find_one(id="Default")
    if row is not None:
        return row
    return None


@connect_db
def get_all_templates(db, offset, limit):
    table = db[TEMPLATES_TABLE]
    return table.find()


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
