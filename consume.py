import boto3
import threading

sqs = boto3.resource('sqs', region_name='us-west-2')
queue = sqs.get_queue_by_name(QueueName='tps-test')

def loop():
    for message in queue.receive_messages(MaxNumberOfMessages=10):
    #  print(message)
        print(message.body)

threading.Thread(target=loop).start()
