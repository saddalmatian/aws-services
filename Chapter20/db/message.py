from .utils import table
from models.schemas import message as message_schema
from ksuid import Ksuid
from boto3.dynamodb.conditions import Key

def create_message(message:message_schema.MessageIn):
    ksuid = Ksuid()
    create_date=ksuid.datetime.strftime("%Y-%m-%d %H:%M:%S")
    response = table.put_item(
        Item={
            "PK":"MESSAGE#"+message.user_name,
            "SK":"MESSAGE#"+create_date,
            "Subject":message.subject,
            "Body":message.body,
            "Unread":True,
            "CreatedAt":create_date,
            "GSI1PK":"MESSAGE#"+message.user_name,
            "GSI1SK":"MESSAGE#"+create_date,
        },
        ConditionExpression="attribute_not_exists(PK)"
    )
    return response

def get_user_message(user_name:str):
    response = table.query(
        KeyConditionExpression=Key("PK").eq("MESSAGE#"+user_name),
    ) 
    return response["Items"]

def mark_message_read(message:message_schema.MessageMarkIn):
    response = table.update_item(
    Key={
        'PK': 'MESSAGE#'+message.user_name,
        'SK': 'MESSAGE#'+str(message.created_at)
    },
    UpdateExpression='SET Unread = :bool REMOVE GSI1PK,GSI1SK',
    ExpressionAttributeValues={
        ":bool":False
    }
)
    return response

def get_user_unread_message(user_name:str):
    response = table.query(
        IndexName="GSI1",
        KeyConditionExpression=Key("GSI1PK").eq("MESSAGE#"+user_name),
    )
    return response["Items"]