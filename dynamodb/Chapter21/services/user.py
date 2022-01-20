from models.schemas import user as user_schemas
from db import user as user_db


def create_user(user: user_schemas.UserIn):
    return user_db.create_user(user)


def get_user(username: str):
    return user_db.get_user(username)


def get_user_org(username: str):
    return user_db.get_user_org(username)


def create_org(org: user_schemas.OrgIn):
    return user_db.create_org(org)


def get_org(orgname: str):
    return user_db.get_org(orgname)


def add_user_org(username: str, orgname: str):
    return user_db.add_user_org(username, orgname)


def get_user_repo(username: str):
    return user_db.get_user_repo(username)


def get_org_repo(orgname: str):
    return user_db.get_org_repo(orgname)
