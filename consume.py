import boto3
import threading
import time

sqs = boto3.resource('sqs', region_name='us-west-2')
queue = sqs.get_queue_by_name(QueueName='tps-test')

def loop():
    while(True):
        for message in queue.receive_messages(MaxNumberOfMessages=10):
        #  print(message)
            print(message.body)
            time.sleep(0.2)
            print(message.delete())

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