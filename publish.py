import boto3
# Get the service resource
sqs = boto3.resource('sqs', region_name='us-west-2')
# get queue
queue = sqs.get_queue_by_name(QueueName='tps-test')

for x in range(100):
  response = queue.send_message(MessageBody=str(x))
