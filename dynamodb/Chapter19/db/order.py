from db import utils
from boto3.dynamodb.conditions import Key
from ksuid.ksuid import Ksuid
import datetime


def get_order_details(order_id):
    response = utils.table.query(
        IndexName="GSI2",
        KeyConditionExpression=Key("GSI2PK").eq("ORDER#"+order_id) & Key("GSI2SK").begins_with("ORDER#"+order_id),
        ProjectionExpression="Amount,NumberItems,#stt,OrderId,ItemId,Price,Description",
        ExpressionAttributeNames={
            "#stt":"Status"
        }
    )
    return response["Items"]


def create_order(order_info,customer_id,order_list):
    number_item=0
    with utils.table.batch_writer() as batch:
        for item in order_list:
            datetime_now = datetime.datetime.now()
            ksuid = Ksuid(datetime_now)
            number_item+=1
            batch.put_item(
                Item={
                    "PK":"ORDER#"+str(ksuid)+"#ITEM#"+item.item_id,
                    "SK":"ORDER#"+str(ksuid)+"#ITEM#"+item.item_id,
                    "OrderID":str(ksuid),
                    "ItemId":item.item_id,
                    "Description":item.description,
                    "Price":item.price,  
                    "GSI2PK":"ORDER#"+str(ksuid),
                    "GSI2SK":"ORDER#"+str(ksuid)+"ITEM#"+item.item_id
                }
            )    

    response = utils.table.put_item(
        Item={
            "PK": "CUSTOMER#"+customer_id,
            "SK": "ORDER#"+str(ksuid),
            "OrderId":str(ksuid),
            "Status":order_info["status"],
            "Amount":order_info["amount"],
            "NumberItems":number_item,
            "GSI1PK":"CUSTOMER#"+customer_id,
            "GSI1SK":"ORDER#"+str(ksuid),
            "GSI2PK":"ORDER#"+str(ksuid),
            "GSI2SK":"ORDER#"+str(ksuid),
        },
    )

    return response

def update_order(order_status,order_id,customer_id):
    response = utils.table.update_item(
        Key={
                'PK': "CUSTOMER#"+customer_id,
                'SK': "ORDER#"+order_id,
            },
        UpdateExpression='SET #stt = :or_stt',
        ExpressionAttributeNames={
            "#stt":"Status"
        },
        ExpressionAttributeValues={
            ':or_stt': order_status
        },
        ConditionExpression="attribute_exists(#stt)"
    )
    return response
