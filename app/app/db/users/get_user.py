from app.utils import resource
from boto3.dynamodb.conditions import Key

def get_user(id):
    response = resource.query(
        KeyConditionExpression=Key('PK').eq(id) & Key('SK').eq(id)
    )
    return(response["Items"][0])
    
  
