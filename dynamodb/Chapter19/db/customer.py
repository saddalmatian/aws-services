from db import utils
from boto3.dynamodb.conditions import Key
from fastapi import status

def get_customer(id:str):
    response = utils.table.query(
        KeyConditionExpression=Key("PK").eq("CUSTOMER#"+id) & Key("SK").eq("CUSTOMER#"+id)
    )
    return response["Items"][0]

def get_customer_order(customer_id:str):
    response = utils.table.query(
        KeyConditionExpression=Key("PK").eq("CUSTOMER#"+customer_id) & Key("SK").begins_with("ORDER#"),
        ProjectionExpression="OrderId,#st,Amount,NumberItems",
        ExpressionAttributeNames={"#st":"Status"},
        Limit=10
    )
    return response["Items"]

def create_customer(customer_info):
    try:
        utils.table.put_item(
            Item={
                "PK":"CUSTOMER#"+customer_info["name"],
                "SK":"CUSTOMER#"+customer_info["name"],
                "Name":customer_info["name"],
                "Age":customer_info["age"],
                "Addresses":customer_info["addresses"],
                "Email":customer_info["email"],
            },
            ConditionExpression="attribute_not_exists(PK)"
        )
        if(customer_info["email"]):
            utils.table.put_item(
                    Item={
                    "PK":"CUSTOMER#"+customer_info["name"]+"#EMAIL#"+customer_info["email"],
                    "SK":"CUSTOMER#"+customer_info["name"]+"#EMAIL#"+customer_info["email"],
                    "Name":customer_info["name"],
                    "Email":customer_info["email"],
                },
                ConditionExpression="attribute_not_exists(PK)"
                )   
    except:
        return status.HTTP_400_BAD_REQUEST
    return status.HTTP_201_CREATED

def delete_email(customer_name):
    customer = utils.table.query(
        KeyConditionExpression=Key("PK").eq("CUSTOMER#"+customer_name),
        ProjectionExpression="Email",
        )
    try:
        utils.table.delete_item(
            Key={
                "PK":"CUSTOMER#"+customer_name+"#EMAIL#"+customer["Items"][0]["Email"],
                "SK":"CUSTOMER#"+customer_name+"#EMAIL#"+customer["Items"][0]["Email"],
            },         
            ConditionExpression="attribute_exists(PK)"
            )

        utils.table.update_item(
            Key={
                'PK': "CUSTOMER#"+customer_name,
                'SK': "CUSTOMER#"+customer_name,
            },
            UpdateExpression='REMOVE Email',
            ConditionExpression="attribute_exists(Email)"
        )    
    except:
        return status.HTTP_400_BAD_REQUEST
    return status.HTTP_200_OK

def update_email(customer_name,customer_email):
    try:
        customer = utils.table.query(
        KeyConditionExpression=Key("PK").eq("CUSTOMER#"+customer_name),
        ProjectionExpression="Email",
        )

        utils.table.delete_item(
             Key={
                "PK":"CUSTOMER#"+customer_name+"#EMAIL#"+customer["Items"][0]["Email"],
                "SK":"CUSTOMER#"+customer_name+"#EMAIL#"+customer["Items"][0]["Email"],
            },         
            ConditionExpression="attribute_exists(PK)"
        )

        utils.table.update_item(
            Key={
                'PK': "CUSTOMER#"+customer_name,
                'SK': "CUSTOMER#"+customer_name,
            },
            UpdateExpression='SET Email = :email',
            ExpressionAttributeValues={
                ':email': customer_email
            },
            ConditionExpression="attribute_exists(Email)"
        )

        utils.table.put_item(
            Item={
                "PK":"CUSTOMER#"+customer_name+"#EMAIL#"+customer_email,
                "SK":"CUSTOMER#"+customer_name+"#EMAIL#"+customer_email,
                "Name":customer_name,
                "Email":customer_email,
            },
            ConditionExpression="attribute_not_exists(PK)"
        )

    except:
        return status.HTTP_400_BAD_REQUEST
    return status.HTTP_201_CREATED


def create_customer_email(customer_name,customer_email):
    try:
        utils.table.put_item(
            Item={
                "PK":"CUSTOMER#"+customer_name+"#EMAIL#"+customer_email,
                "SK":"CUSTOMER#"+customer_name+"#EMAIL#"+customer_email,
                "Name":customer_name,
                "Email":customer_email,
            },
            ConditionExpression="attribute_not_exists(PK)"
        )

        utils.table.update_item(
            Key={
                'PK': "CUSTOMER#"+customer_name,
                'SK': "CUSTOMER#"+customer_name,
            },
            UpdateExpression='SET Email = :email',
            ExpressionAttributeValues={
                ':email': customer_email
            }
        )
    except:
        return status.HTTP_400_BAD_REQUEST
    return status.HTTP_201_CREATED