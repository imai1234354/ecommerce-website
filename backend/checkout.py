import json
import boto3

def lambda_handler(event, context):
    user = event['requestContext']['authorizer']['claims']['cognito:username']
    
    dynamodb = boto3.resource('dynamodb')
    cart_table = dynamodb.Table('CartTable')
    
    # Fetch cart items
    response = cart_table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key('userId').eq(user)
    )
    
    # Process checkout (simple example)
    cart_items = response['Items']
    cart_table.delete_item(Key={'userId': user})
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Checkout successful', 'items': cart_items})
    }
