import boto3

resource = boto3.resource(
    "dynamodb"
)

client = boto3.client(
    "dynamodb"
)

# response = resource.create_table(
#     TableName="Orders",
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
#     ProvisionedThroughput={
#         "ReadCapacityUnits":1,
#         "WriteCapacityUnits":1
#     }
# )

table = resource.Table("Orders")

# response = table.put_item(
#     Item={
#         "PK":"CUSTOMERID1#",
#         "SK":"CUSTOMERID1#",
#         "Name":"GiangHoaTran",
#         "Age":21,
#         "Addresses":{
#             "home":{
#                 "Street":"Ngo Gia Tu",
#                 "City":"Can Tho",
#                 "Nation":"Viet Nam"
#             },
#             "business":{
#                 "Street":"3/2 Street",
#                 "City":"Can Tho",
#                 "Nation":"Viet Nam"
#             },
#         },
#     }
# )

# with table.batch_writer() as batch:
#     batch.put_item(
#         Item={
#             "PK":"CUSTOMERID1#",
#             "SK":"ORDER1#",
#             "OrderID":"order1",
#             "Status":"DELIEVERED",
#             "Amount":decimal.Decimal("98.54"),
#             "NumberItems":4
#         }
#     ),
#     batch.put_item(
#         Item={
#             "PK":"CUSTOMERID1#",
#             "SK":"ORDER2#",
#             "OrderID":"order2",
#             "Status":"CANCELED",
#             "Amount":decimal.Decimal("20.25"),
#             "NumberItems":5
#         }
#     )

# table.delete_item(
#     Key={
#         "PK":"CUSTOMERID1#",
#         "SK":"ORDER1#",
#     }
# )

# table.update_item(
#     Key={
#         "PK":"CUSTOMERID1#",
#         "SK":"ORDER1#",
#     },
#     AttributeUpdates={
#         "GSI1PK":{
#             "Value":"ORDER1#",
#         },
#         "GSI1SK":{
#             "Value":"ITEM#order1#123",
#         },
#     },
# )

# client.update_table(
#     TableName="Orders",
#     AttributeDefinitions=[
#         {
#             "AttributeName":"GSI2PK",
#             "AttributeType":"S",
#         },
#         {
#             "AttributeName":"GSI2SK",
#             "AttributeType":"S"
#         }
#     ],
#     GlobalSecondaryIndexUpdates=[
#         {
#             "Create":{
#                 "IndexName":"GSI2",
#                 "ProvisionedThroughput":{
#                     "WriteCapacityUnits": 1,
#                     "ReadCapacityUnits": 1
#                 },
#                 "KeySchema":[
#                     {
#                         "AttributeName":"GSI2PK",
#                         "KeyType":"HASH",
#                     },
#                     {
#                         "AttributeName":"GSI2SK",
#                         "KeyType":"RANGE"
#                     }
#                 ],
#                 "Projection":{"ProjectionType":"ALL"}
#             }
#         }
#     ]
# )
   
# response = table.query(
#     IndexName="GSI1",
#     KeyConditionExpression=Key("GSI1PK").eq('ORDER1#')
# )
# items=response["Items"][0]
# print(items)