from db import message as message_db

def create_message(message):
    return message_db.create_message(message)


def get_user_message(user_name):
    return message_db.get_user_message(user_name) 

def mark_message_read(message):
    return message_db.mark_message_read(message)

def get_user_unread_message(user_name):
    return message_db.get_user_unread_message(user_name) 