from db import user as user_db

def create_user(user):
    return user_db.create_user(user)


def get_user(user):
    return user_db.get_user(user)