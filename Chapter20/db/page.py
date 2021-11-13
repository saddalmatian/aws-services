from .utils import table
from models.schemas import page as page_schema

def add_featured_deals(page,page_type:str):
    # try:
    #     table.put_item(
    #         Item={
    #             "PK":"FRONTPAGE",
    #             "SK":"FRONTPAGE",
    #             "FeaturedDeals":page.featured_deals,
    #         },
    #         ConditionExpression="attribute_not_exists(PK)"
    #     )
    #     table.put_item(
    #         Item={
    #             "PK":"EDITORSCHOICE",
    #             "SK":"EDITORSCHOICE",
    #             "FeaturedDeals":page.featured_deals,
    #         },
    #         ConditionExpression="attribute_not_exists(PK)"
    #     )
    # except:
    #     print("Containing all pages had created!")

    # response = table.update_item(
    #     Key={
    #         "PK":page_type.upper(),
    #         "SK":page_type.upper(),
    #     },
    #     UpdateExpression="SET FeaturedDeals = :ft",
    #     ExpressionAttributeValues={
    #         ":ft":page.featured_deals
    #     },
    #     ConditionExpression="attribute_exists(PK)"
    # )
    return "response"
    

# def get_page(page_name):
#     response = table.get_item(
#         Key={
#             'PK': 'BRAND#'+page_name,
#             'SK': 'BRAND#'+page_name
#         }
#     )
#     return response["Item"]
