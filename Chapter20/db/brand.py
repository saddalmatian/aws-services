from .utils import table
from models.schemas import brand as brand_schema



def create_brand(brand:brand_schema.BrandIn):
    # try:
    #     table.put_item(
    #         Item={
    #             "PK":"BRANDS",
    #             "SK":"BRANDS",
    #             "Brands":[],
    #         },
    #         ConditionExpression="attribute_not_exists(PK)"
    #     )
    # except:
    #     print("Containing all brands had created!")

    response_first = table.put_item(
        Item={
            "PK":"BRAND#"+brand.brand_name,
            "SK":"BRAND#"+brand.brand_name,
            "BrandName":brand.brand_logo_url,
            "BrandLogoUrl":brand.brand_logo_url,
            "LikeCount":0
        },
        ConditionExpression="attribute_not_exists(PK)",
    )
    if(response_first["ResponseMetadata"]["HTTPStatusCode"]==200):
        response = table.update_item(
        Key={
            'PK': "BRANDS",
            'SK': "BRANDS"
        },
        UpdateExpression="SET Brands = list_append(Brands, :brand)",
        ExpressionAttributeValues={
            ':brand': [brand.brand_name],
        },
    )
        return response
    else:
        return response_first


def get_brand(brand_name):
    response = table.get_item(
        Key={
            'PK': 'BRAND#'+brand_name,
            'SK': 'BRAND#'+brand_name
        }
    )
    return response["Item"]

def get_all_brand():
    response = table.get_item(
        Key={
            'PK': 'BRANDS',
            'SK': 'BRANDS'
        },
        ProjectionExpression="Brands"
    )
    return response["Item"]["Brands"]

def add_brand_like(user_id:str,brand_name:str):
    table.put_item(
        Item={
            "PK":"BRANDLIKE#"+brand_name+"#"+user_id,
            "SK":"BRANDLIKE#"+brand_name+"#"+user_id,
        },
        ConditionExpression="attribute_not_exists(PK)"
    )   
    response = table.update_item(
        Key={
            "PK":"BRAND#"+brand_name,
            "SK":"BRAND#"+brand_name
        },
        UpdateExpression="SET LikeCount = LikeCount + :lk",
        ExpressionAttributeValues={
            ":lk":1
        },
        ConditionExpression="attribute_exists(PK)"
    )

    return response

def add_brand_watch(user_id:str,brand_name:str):
    response = table.put_item(
        Item={
            "PK":"BRANDWATCH#"+brand_name,
            "SK":"USER#"+user_id,
        },
        ConditionExpression="attribute_not_exists(PK)"
    )   

    return response
