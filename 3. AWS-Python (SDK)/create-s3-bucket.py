import boto3

s3_client = boto3.client('s3')

response = s3_client.create_bucket( ACL = 'private', Bucket = 'bucket-from-python-sdk')

print(response)