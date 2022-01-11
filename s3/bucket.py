import boto3
import json
import os


client = boto3.client('s3')
resource = boto3.resource('s3')
bucket = resource.Bucket('nembucket')


def print_json(response: str):
    print(json.dumps(response, indent=4, sort_keys=True, default=str))

# Create a bucket
# response = bucket.create(
#     CreateBucketConfiguration={
#         'LocationConstraint': 'ap-southeast-1',
#     },
# )
# print_json(response)


# Upload an object
# bucket.upload_file('text.txt', 'hello.txt')


# Download an object
# resource.meta.client.download_file('nembucket', 'manage.py', 'manage.py')
print(os.listdir('env'))


# List objects
# for obj in bucket.objects.all():
#     print(obj.key)


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
