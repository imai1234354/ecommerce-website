import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ProductsTable')
    
    response = table.scan()
    products = response['Items']
    
    return {
        'statusCode': 200,
        'body': json.dumps(products)
    }
