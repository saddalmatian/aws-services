from .utils import table
from models.schemas import page as page_schema

def add_featured_deals(page:page_schema.PageIn):
    # try:
    #     table.put_item(
    #         Item={
    #             "PK":"FRONTPAGE",
    #             "SK":"FRONTPAGE",
    #             "FeaturedDeals":[],
    #         },
    #         ConditionExpression="attribute_not_exists(PK)"
    #     )
    #     table.put_item(
    #         Item={
    #             "PK":"EDITORSCHOICE",
    #             "SK":"EDITORSCHOICE",
    #             "FeaturedDeals":[],
    #         },
    #         ConditionExpression="attribute_not_exists(PK)"
    #     )
    # except:
    #     print("Containing all pages had created!")
    response = table.update_item(
        Key={
            "PK":page["PageType"].upper(),
            "SK":page["PageType"].upper(),
        },
        UpdateExpression="SET FeaturedDeals = :ft",
        ExpressionAttributeValues={
            ":ft":page["FeaturedDeals"]
        },
        ConditionExpression="attribute_exists(PK)"
    )
    
    return response
    

def get_featured_deals(page_name):
    page_name=page_name.upper()
    response = table.get_item(
        Key={
            'PK': page_name,
            'SK': page_name
        }
    )
    return response["Item"]
