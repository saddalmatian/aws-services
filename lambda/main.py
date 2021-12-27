import boto3
import json


def print_json(response):
    print(json.dumps(response,indent=4,sort_keys=True,default=str))


client = boto3.client('lambda')



# Get zip function (handler)
with open('lambda.zip','rb') as f:
    zipped_code = f.read()


# Create function
# response = client.create_function(
#     FunctionName='helloWorldLambda',
#     Runtime='python3.9',
#     Role='arn:aws:iam::769253686157:role/hoaLambdaBasicRole',
#     Handler='handler.lambda_handler',
#     Code=dict(ZipFile=zipped_code),
#     Timeout=300
# )
# print_json(response)


# Update function
# with open('lambda.zip', 'rb') as f:
#     zipped_code = f.read()
# response = client.update_function_code(
#     FunctionName='helloWorldLambda',
#     ZipFile=zipped_code
# )


