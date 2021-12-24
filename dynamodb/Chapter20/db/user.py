from .utils import table
from models.schemas import user as user_schema
from datetime import datetime

def create_user(user:user_schema.UserIn):
    create_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response = table.put_item(
        Item={
            "PK":"USER#"+user.user_name,
            "SK":"USER#"+user.user_name,
            "Username":user.user_name,
            "CreatedAt":create_date,
            "UserIndex":"USER#"+user.user_name
        },
        ConditionExpression="attribute_not_exists(PK)"
    )
    return response

def get_user(user_name:str):
    response = table.get_item(
        Key={
            "PK":"USER#"+user_name,
            "SK":"USER#"+user_name
        }
    )
    return response["Item"]