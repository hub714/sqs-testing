import boto3
client = boto3.client('sqs', region_name='us-west-2')
response = client.get_queue_url(QueueName='tps-test')
url = response['QueueUrl']
response = client.purge_queue(QueueUrl=url)
