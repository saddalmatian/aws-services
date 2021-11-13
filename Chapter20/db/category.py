from .utils import table
from models.schemas.category import CategoryIn

def get_category(category_name):
    response = table.get_item(
        Key={
            'PK': 'CATEGORY#'+category_name,
            'SK': 'CATEGORY#'+category_name
        }
    )
    return response["Item"]

def create_category(category:CategoryIn):
    response = table.put_item(
        Item={
            "PK":"CATEGORY#"+category.category_name,
            "SK":"CATEGORY#"+category.category_name,
            "CategoryName":category.category_name,
            "FeaturedDeals":category.featured_deals
        },
        ConditionExpression="attribute_not_exists(PK)"
    )
    return response

def add_category_like(user_id:str,category_name:str):
    response = table.put_item(
        Item={
            "PK":"CATEGORYLIKE#"+category_name+"#"+user_id,
            "SK":"CATEGORYLIKE#"+category_name+"#"+user_id,
        },
        ConditionExpression="attribute_not_exists(PK)"
    )
    return response

def add_category_watch(user_id:str,category_name:str):
    response = table.put_item(
        Item={
            "PK":"CATEGORYWATCH#"+category_name,
            "SK":"USER#"+user_id
        },
        ConditionExpression="attribute_not_exists(PK)"
    )
    return response

def add_featured_deals(deal_list:list,category_name:str):
    response = table.update_item(
        Key={
            "PK":"CATEGORY#"+category_name,
            "SK":"CATEGORY#"+category_name,
        },
        UpdateExpression="SET FeaturedDeals = :dl",
        ExpressionAttributeValues={
            ":dl":deal_list
        },
        ConditionExpression="attribute_exists(PK)"
    )
    return response