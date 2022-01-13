import boto3,json

client=boto3.client('lambda')


# This is test event when you invoke
test_event={
    "key1":"PhantomAL"
}

# Use to invoke a lambda function
response = client.invoke(
    FunctionName='helloWorldLambda',
    Payload=json.dumps(test_event),
)


# return response
print(response['Payload'].read().decode("utf-8"))
