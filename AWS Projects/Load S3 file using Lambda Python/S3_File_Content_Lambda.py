import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
   Bucket_Name = 'transaction-viky'
   Key_Name = 'transaction.json'

   response = s3.get_object(Bucket = Bucket_Name, Key = Key_Name)

   content = response['Body']
   content = json.loads(content.read())
   
   print("--------------CONTENT--------------")
   print(content)
   print("-----------------------------------")
   
   
   transactions = content['transactions']
   
   i=1
   for record in transactions:
       print("------------RECORD -",+i ,'------------')
       print("Transaction Type   : " + record['transactionType'])
       print("Transaction Amount : " + str(record['amount']))
       i+=1
   print("-----------------------------------")