import json
import boto3

def lambda_handler(event, context):
    user = event['requestContext']['authorizer']['claims']['cognito:username']
    product_id = event['body']['productId']
    
    dynamodb = boto3.resource('dynamodb')
    cart_table = dynamodb.Table('CartTable')
    
    response = cart_table.update_item(
        Key={'userId': user, 'productId': product_id},
        UpdateExpression="set quantity = if_not_exists(quantity, :start) + :inc",
        ExpressionAttributeValues={':start': 0, ':inc': 1},
        ReturnValues="UPDATED_NEW"
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(response['Attributes'])
    }
