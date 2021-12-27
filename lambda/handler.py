import os


# lambda response
def lambda_handler(event, context):
    return{
        'statusCode':200,
        'body':event['key1']
    }


# Zip file
os.system('zip lambda.zip handler.py')