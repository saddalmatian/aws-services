from models.schemas import user as user_schema
from db.utils import table
from boto3.dynamodb.conditions import Key
from datetime import datetime
created_time = datetime.now().strftime("%d-%m-%Y %H-%M-%S")


def create_user(user: user_schema.UserIn):
    response = table.put_item(
        Item={
            "PK": "ACCOUNT#"+user.username,
            "SK": "ACCOUNT#"+user.username,
            "Type": "User",
            "Username": user.username,
            "Organization": {},
            "CreatedAt": created_time,
            "GSI3PK": "ACCOUNT#"+user.username,
            "GSI3SK": "ACCOUNT#"+user.username,
        },
        ConditionExpression="attribute_not_exists(PK)"
    )
    return response


def get_user(username: str):
    response = table.query(
        KeyConditionExpression=Key("PK").eq(
            "ACCOUNT#"+username) & Key("SK").eq("ACCOUNT#"+username),
        FilterExpression="#type = :type",
        ExpressionAttributeNames={
            "#type": "Type"
        },
        ExpressionAttributeValues={
            ":type": "User"
        }
    )
    return response["Items"][0]


def add_user_org(username: str, orgname: str):
    table.put_item(
        Item={
            "PK": "ACCOUNT#"+orgname,
            "SK": "MEMBERSHIP#"+username,
            "Username": username,
            "CreatedAt": created_time,
            "Role": "Member"
        },
        ConditionExpression="attribute_not_exists(PK)"
    )
    response = table.update_item(
        Key={
            "PK": "ACCOUNT#"+username,
            "SK": "ACCOUNT#"+username,
        },
        UpdateExpression="SET Organization.#orgname = :plan",
        ExpressionAttributeNames={
            "#orgname": orgname
        },
        ExpressionAttributeValues={
            ":plan": "Member"
        },
    )
    return response


def create_org(org: user_schema.OrgIn):
    response = table.put_item(
        Item={
            "PK": "ACCOUNT#"+org.orgname,
            "SK": "ACCOUNT#"+org.orgname,
            "Type": "Organization",
            "OrganizationName": org.orgname,
            "CreatedAt": created_time,
            "GSI3PK": "ACCOUNT#"+org.orgname,
            "GSI3SK": "ACCOUNT#"+org.orgname,
        },
        ConditionExpression="attribute_not_exists(PK)"
    )
    return response


def get_org(orgname: str):
    response = table.query(
        KeyConditionExpression=Key("PK").eq(
            "ACCOUNT#"+orgname) & Key("SK").eq("ACCOUNT#"+orgname),
        FilterExpression="#type = :type",
        ExpressionAttributeNames={
            "#type": "Type"
        },
        ExpressionAttributeValues={
            ":type": "Organization"
        }
    )
    return response["Items"][0]


def get_user_org(username: str):
    response = table.query(
        KeyConditionExpression=Key("PK").eq(
            "ACCOUNT#"+username) & Key("SK").eq("ACCOUNT#"+username),
        ProjectionExpression="Organization"
    )
    return response["Items"]


def get_user_repo(username: str):
    response = table.query(
        IndexName="GSI3",
        KeyConditionExpression=Key("GSI3PK").eq(
            "ACCOUNT#"+username) & Key("GSI3SK").begins_with("#"),
    )
    return response["Items"]


def get_org_repo(orgname: str):
    response = table.query(
        IndexName="GSI3",
        KeyConditionExpression=Key("GSI3PK").eq(
            "ACCOUNT#"+orgname) & Key("GSI3SK").begins_with("#"),
    )
    return response["Items"]
