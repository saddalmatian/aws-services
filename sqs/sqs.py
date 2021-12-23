import boto3
import json

def print_json(response: str):
    print(json.dumps(response,indent=4,sort_keys=True,default=str))


client = boto3.client('sqs')
resource = boto3.resource('sqs')


#Create fifo queue
# resource.create_queue(
#     QueueName='anotherqueue.fifo',
#     Attributes={
#         'FifoQueue':'True',
#     },
# )

#Using an existing queue
queue = resource.get_queue_by_name(QueueName='queue.fifo')
# print(queue)

#List all queue
# for queue in resource.queues.all():
#     print(queue)


#Send message
# response = queue.send_message(
#     MessageBody='AnotherHelloWorldZasas2',
#     MessageGroupId="queueGroup",
#     MessageDeduplicationId="queueDedup12"
# )
# print_json(response)

#Receive message
# for message in queue.receive_messages():
    # print(message.body)
#Delete message
    # message.delete()
