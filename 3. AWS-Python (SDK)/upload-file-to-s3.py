import boto3

s3_client = boto3.client('s3')

response = s3_client.upload_file(r'G:\\Learning\\AWS-Python (SDK)\\files\\10kSamplejson.json','bucket-from-python-sdk','json/sample.json')

print(response)