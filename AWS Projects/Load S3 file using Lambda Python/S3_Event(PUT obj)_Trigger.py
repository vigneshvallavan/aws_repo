import json
import boto3
import urllib

def lambda_handler(event, context):
   
   s3 = boto3.client('s3')
    
   Bucket_Name = event['Records'][0]['s3']['bucket']['name']
   Key_Name = event['Records'][0]['s3']['object']['key']
   Key_Name = urllib.parse.unquote_plus(Key_Name, encoding = 'utf-8')

   response = s3.get_object(Bucket = Bucket_Name, Key = Key_Name)

   content = response['Body'].read().decode()
   jsonObject = json.loads(content)
   
   print("--------------------------------------")
   print("  These are the content of the file ; \n", jsonObject)
   print("--------------------------------------")