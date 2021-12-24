from datetime import date
from .utils import table
from models.schemas import deal as deal_schema
from ksuid import Ksuid
from boto3.dynamodb.conditions import Key


def create_deal(deal:deal_schema.DealIn):
    ksuid = Ksuid()
    response = table.put_item(
        Item={
            "PK":"DEAL#"+str(ksuid),
            "SK":"DEAL#"+str(ksuid),
            "DealID":str(ksuid),
            "Title":deal.title,
            "Link":deal.link,
            "Price":deal.price,
            "Category":deal.category,
            "Brand":deal.brand,
            "CreatedAt":str(ksuid.datetime.strftime("%Y-%m-%d %H:%M")),
            "GSI1PK":"DEALS#"+str(ksuid.datetime.replace(hour=0, minute=0).strftime("%Y-%m-%d %H:%M")),
            "GSI1SK":"DEAL#"+str(ksuid),
            "GSI2PK":"BRAND#"+deal.brand+"#"+str(ksuid.datetime.replace(hour=0, minute=0).strftime("%Y-%m-%d %H:%M")),
            "GSI2SK":"DEAL#"+str(ksuid),
            "GSI3PK":"CATEGORY#"+deal.category+"#"+str(ksuid.datetime.replace(hour=0, minute=0).strftime("%Y-%m-%d %H:%M")),
            "GSI3SK":"DEAL#"+str(ksuid),
        },
        ConditionExpression="attribute_not_exists(PK)"
    )

    return response

def get_deal(deal_id):
    response = table.get_item(
        Key={
            'PK': 'DEAL#'+deal_id,
            'SK': 'DEAL#'+deal_id
        }
    )
    return response["Item"]

def fetch_deal_date(date:date):
    response = table.query(
        IndexName="GSI1",
        KeyConditionExpression=Key("GSI1PK").eq("DEALS#"+str(date)+" 00:00"),
        Limit=10
    )
    return response["Items"]

def fetch_deal_brand(brand:str):
    ksuid = Ksuid()
    response = table.query(
        IndexName="GSI2",
        KeyConditionExpression=Key("GSI2PK").eq("BRAND#"+brand+"#"+str(ksuid.datetime.replace(hour=0, minute=0).strftime("%Y-%m-%d %H:%M"))),
        Limit=10
    )
    return response["Items"]

def fetch_deal_category(category:str):
    ksuid = Ksuid()
    response = table.query(
        IndexName="GSI3",
        KeyConditionExpression=Key("GSI3PK").eq("CATEGORY#"+category+"#"+str(ksuid.datetime.replace(hour=0, minute=0).strftime("%Y-%m-%d %H:%M"))),
        Limit=10
    )
    return response["Items"] 