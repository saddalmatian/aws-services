import ksuid
from .utils import table
from models.schemas import message as message_schema
from datetime import datetime
from ksuid import Ksuid

def create_message(user_name:str,message:message_schema.MessageIn):
    ksuid = Ksuid()
    create_date=ksuid.datetime.strftime("%Y-%m-%d %H:%M:%S")
    response = table.put_item(
        Item={
            "PK":"MESSAGE#"+user_name,
            "SK":"MESSAGE#"+str(ksuid)+"#"+create_date,
            "Subject":message.subject,
            "Body":message.body,
            "Unread":True,
            "GSI1PK":"MESSAGE#"+user_name,
            "GSI1SK":"MESSAGE#"+str(ksuid),
        },
        ConditionExpression="attribute_not_exists(PK)"
    )
    return response

def get_message(message_name:str):
    response = table.get_item(
        Key={
            "PK":"USER#"+message_name,
            "SK":"USER#"+message_name
        }
    ) 
    return response["Item"]