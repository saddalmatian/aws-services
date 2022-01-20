from db import login as db_login


def verify_password(username, password):
    return db_login.verify_password(username, password)


def generate_token(username):
    return db_login.generate_token(username)
