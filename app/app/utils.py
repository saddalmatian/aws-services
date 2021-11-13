import boto3

client = boto3.client(
    "dynamodb"
)

resource = boto3.resource(
    "dynamodb"
).Table("Login") 

