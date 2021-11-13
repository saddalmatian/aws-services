from utils import client,resource
import json
# -----Create table with global secondary indexes NOT implemented-----
# response = client.create_table(
#     AttributeDefinitions=[
#         {
#             "AttributeName":"PK",
#             "AttributeType":"S"
#         },
#         {
#             "AttributeName":"SK",
#             "AttributeType":"S"
#         }
#     ],
#     TableName="Organization",
#     KeySchema=[
#         {
#             "AttributeName":"PK",
#             "KeyType":"HASH"
#         },
#         {
#             "AttributeName":"SK",
#             "KeyType":"RANGE"
#         }
#     ],
#     ProvisionedThroughput= 
#         {
#             "WriteCapacityUnits": 1,
#             "ReadCapacityUnits": 1
#         },
# )

# -----Write table with transact_write_items-----
# response = client.transact_write_items(
#     TransactItems=[
#     {
#     'Put': {
#     'TableName': 'Organization',
#     'Item': {
#         'PK': { "S" : "ORG#MICROSOFT" },
#         'SK': { "S" : "METADATA#MICROSOFT" },
#         'OrgName':{"S" : "Microsoft"},
#         "PlanType":{"S" : "Enterprise"}
#     },
#     'ConditionExpression': 'attribute_not_exists(PK)'
#         }
#     },
#     {
#     'Put': {
#     'TableName': 'Organization',
#     'Item': {
#         'PK': { "S" : "ORG#MICROSOFT" },
#         'SK': { "S" : "USER#BILGATES" },
#         "UserName":{"S" : "Bill Gates"},
#         "UserType":{"S":"Member"},
#         "GSI1":{"S":"USER"},
#         "GSI2":{"S":"USER#BILGATES"}
#     },
#     'ConditionExpression': 'attribute_not_exists(PK)'
#         }
#     },
#       {
#     'Put': {
#     'TableName': 'Organization',
#     'Item': {
#         'PK': { "S" : "ORG#MICROSOFT" },
#         'SK': { "S" : "USER#SATYANADELLA"},
#         "UserName":{"S" : "Satya Nadella"},
#         "UserType":{"S":"Admin"},
#         "GSI1":{"S":"USER"},
#         "GSI2":{"S":"USER#SATYANADELLA"}
#     },
#     'ConditionExpression': 'attribute_not_exists(PK)'
#         }
#     },
#     {
#     'Put': {
#     'TableName': 'Organization',
#     'Item': {
#         'PK': { "S" : "ORG#AMAZON" },
#         'SK': { "S" : "METADATA#AMAZON"},
#         "OrgName":{"S" : "Amazon"},
#         "PlanType":{"S":"Pro"}
#     },
#     'ConditionExpression': 'attribute_not_exists(PK)'
#         }
#     },
#     {
#     'Put': {
#     'TableName': 'Organization',
#     'Item': {
#         'PK': { "S" : "ORG#AMAZON" },
#         'SK': { "S" : "USER#JEFFBEZOS"},
#         "UserName":{"S" : "Jeff Bezos"},
#         "UserType":{"S":"Admin"},
#         "GSI1":{"S":"USER"},
#         "GSI2":{"S":"USER#JEFFBEZOS"}
#     },
#     'ConditionExpression': 'attribute_not_exists(PK)'
#         }
#     },
# ]
# )

# -----Update table with GSI-----
# response = client.update_table(
#     AttributeDefinitions=[
#         {
#             'AttributeName':'GSI1',
#             'AttributeType':'S'
#         },
#         {
#             'AttributeName':'GSI2',
#             'AttributeType':'S'
#         }
#     ],
#     TableName = 'Organization',
#     GlobalSecondaryIndexUpdates=[
#         {
#             'Create': {
#                 'IndexName': 'GSI',
#                 'KeySchema': [
#                     {
#                         'AttributeName': 'GSI1',
#                         'KeyType': 'HASH'
#                     },
#                     {
#                         'AttributeName': 'GSI2',
#                         'KeyType': 'RANGE'
#                     },
#                 ],
#                 'Projection': {
#                     'ProjectionType': 'ALL'
#                 },
#                 'ProvisionedThroughput': {
#                     'ReadCapacityUnits': 1,
#                     'WriteCapacityUnits': 1
#                 }
#             }
#         }
#     ]
# )

# -----Delete item in table-----
# response = client.delete_item(
#     TableName='Movies',
#     Key={
#     "PK": { "S": "myuser" },
#     "SK": { "S": "Bob G. User" }
#     }
# )

# -----Delete table-----
# response = client.delete_table(
#     TableName="Organization"
# )

# -----Query with GSI-----
# response = client.query(
#     TableName="Organization",
#     IndexName="GSI",
#     KeyConditionExpression="GSI1 = :pk",
#     ExpressionAttributeValues={
#         ":pk":{"S":"USER"}
#     }
# )

# -----Scan table-----
# response = client.scan(
#     TableName="Organization",
#     IndexName="GSI"
# )

# -----Print item-----
# print(json.dumps(response,sort_keys=True,indent=4))
