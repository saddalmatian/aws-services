from utils import client,resource
import json

# -----GSI-----
# response = client.create_table(   
#     TableName="First",
#     AttributeDefinitions=[
#         {
#             "AttributeName":"PK",
#             "AttributeType":"S"
#         },
#         {
#             "AttributeName":"SK",
#             "AttributeType":"S"
#         },
#         {
#             "AttributeName":"GSI",
#             "AttributeType":"S"
#         }
#     ],
#     KeySchema=[
#         {
#             "AttributeName":"PK",
#             "KeyType":"HASH"
#         },
#         {
#             "AttributeName":"SK",
#             "KeyType":"RANGE"
#         },
#     ],
#     GlobalSecondaryIndexes=[
#         {
#             "IndexName":"USER",
#             "KeySchema":[
#                 {
#                     "AttributeName":"GSI",
#                     "KeyType":"HASH"
#                 }
#             ],
#             "ProvisionedThroughput":{
#                 "ReadCapacityUnits":1,
#                 "WriteCapacityUnits":1
#             },
#             "Projection":{
#                 "ProjectionType":"ALL",
#                 # "NonKeyAttributes":[
#                 #     "UserName","UserType"
#                 # ]
#             }
#         }
#     ],
#     ProvisionedThroughput={
#                 "ReadCapacityUnits":1,
#                 "WriteCapacityUnits":1
#             }
# )

# -----Write table with transact_write_items-----
# response = client.transact_write_items(
#     TransactItems=[
#     {
#         "Put":{
#             "TableName":"First",
#             "Item":{
#                 "PK":{"S":"ORG#MICROSOFT"},
#                 "SK":{"S":"METADATA#MICROSOFT"},
#                 "OrgName":{"S":"Microsoft"},
#                 "PlanType":{"S":"Enterprise"},
#             },
#             "ConditionExpression":"attribute_not_exists(PK)"
#         }
#     },
#     {
#         "Put":{
#             "TableName":"First",
#             "Item":{
#                 "PK":{"S":"ORG#MICROSOFT"},
#                 "SK":{"S":"USER#BILLGATES"},
#                 "UserName":{"S":"Bill Gates"},
#                 "UserType":{"S":"Member"},
#                 "GSI":{"S":"USER"}
#             },
#             "ConditionExpression":"attribute_not_exists(PK)"
#         }
#     },    
#     {
#         "Put":{
#             "TableName":"First",
#             "Item":{
#                 "PK":{"S":"ORG#MICROSOFT"},
#                 "SK":{"S":"USER#SATYANADELLA"},
#                 "UserName":{"S":"Satya Nadella"},
#                 "UserType":{"S":"Admin"},
#                 "GSI":{"S":"USER"}
#             },
#             "ConditionExpression":"attribute_not_exists(PK)"
#         }
#     },
#     {
#         "Put":{
#             "TableName":"First",
#             "Item":{
#                 "PK":{"S":"ORG#AMAZON"},
#                 "SK":{"S":"METADATA#AMAZON"},
#                 "OrgName":{"S":"Amazon"},
#                 "PlanType":{"S":"Pro"},
#             },
#             "ConditionExpression":"attribute_not_exists(PK)"
#         }
#     },
#     {
#         "Put":{
#             "TableName":"First",
#             "Item":{
#                 "PK":{"S":"ORG#AMAZON"},
#                 "SK":{"S":"USER#JEFFBEZOS"},
#                 "UserName":{"S":"Jeff Bezos"},
#                 "UserType":{"S":"Admin"},
#                 "GSI":{"S":"USER"}
#             },
#             "ConditionExpression":"attribute_not_exists(PK)"
#         }
#     },    
#     ],
# ) 
# -----Query table and return all the users inside the specific organization-----
# response = client.query(
#     TableName="First",
#     KeyConditionExpression="PK=:pk and begins_with(SK,:sk)",
#     ExpressionAttributeValues={
#         ":pk":{"S":"ORG#MICROSOFT"},
#         ":sk":{"S":"USER#"}
#     }
# )
# -----Change table's item-----
# response = client.update_item(
#     TableName="First",
#     Key={
#             "PK":{"S":"ORG#MICROSOFT"},
#             "SK":{"S":"USER#BILLGATES"}
#         },
#     AttributeUpdates={
#         "UserName":{
#             "Value":{
#                 "S":"Not BillGates"
#             }
#         }
#     }
# )
# -----Query table using GSI-----
# response = client.query(
#     TableName="First",
#     IndexName="USER",
#     KeyConditionExpression="GSI=:gsi",
#     ExpressionAttributeValues={
#         ":gsi":{"S":"USER"}
#     }
# )

# -----Print item-----
# print(json.dumps(response,sort_keys=True,indent=4))