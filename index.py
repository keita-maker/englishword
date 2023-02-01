import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('sample_table')

def handler(event, context):
    operation = event["method"]
    if operation == 'GET':
        response = table.scan()
        return response
        
    elif operation == 'POST':
        table.put_item(Item={'id': event["body"]["Item"]["id"], 'name': event["body"]["Item"]["name"]})
        
    else:
        table.delete_item(
            Key = {
                'id':event["body"]["Item"]["id"],
                'name':event["body"]["Item"]["name"]
            }
        )