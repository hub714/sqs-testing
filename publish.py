import boto3
import threading
# Get the service resource
sqs = boto3.resource('sqs', region_name='us-west-2')
# get queue
queue = sqs.get_queue_by_name(QueueName='tps-test')

def loop():
    for x in range(10000):
        response = queue.send_message(MessageBody=str(x))

threading.Thread(target=loop).start()
threading.Thread(target=loop).start()
threading.Thread(target=loop).start()
threading.Thread(target=loop).start()
threading.Thread(target=loop).start()
threading.Thread(target=loop).start()
threading.Thread(target=loop).start()
threading.Thread(target=loop).start()
threading.Thread(target=loop).start()
threading.Thread(target=loop).start()