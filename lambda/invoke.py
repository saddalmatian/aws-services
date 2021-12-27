import boto3,json

client=boto3.client('lambda')

test_event={
    "key1":"PhantomAL"
}


response = client.invoke(
    FunctionName='helloWorldLambda',
    Payload=json.dumps(test_event),
)


# return response
print(response['Payload'].read().decode("utf-8"))