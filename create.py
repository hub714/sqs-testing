import boto3

# Get the service resource
sqs = boto3.resource('sqs', region_name='us-west-2')

# Create the queue. This returns an SQS.Queue instance
queue = sqs.create_queue(QueueName='tps-test')
