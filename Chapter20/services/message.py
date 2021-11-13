from db import message as message_db

def create_message(user_name,message):
    return message_db.create_message(user_name,message)


def get_message(message):
    return message_db.get_message(message)