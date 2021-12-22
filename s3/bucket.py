import boto3
import json


client = boto3.client('s3')
resource = boto3.resource('s3')
bucket = resource.Bucket('gianghoatran')

def print_json(response :str):
    print(json.dumps(response, indent=4, sort_keys=True, default=str))


# Upload an object 
# bucket.upload_file('text.txt', 'hello.txt')


# Delete an object
# response = bucket.delete_objects(
#     Delete={
#         'Objects': [
#             {
#                 'Key': 'hello.txt',
#             },
#         ],
#     },
# )
# print_json(response)


# Load bucket
# response = client.list_buckets()
# print_json(response)


# Delete bucket (must empty it first)
# response = bucket.delete()
# print_json(response)