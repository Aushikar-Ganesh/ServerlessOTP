import boto3
import os
import time

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ['TABLE_NAME']

def lambda_handler(event, context):
    phone_number = event['queryStringParameters']['phone']
    user_otp = event['queryStringParameters']['otp']

    table = dynamodb.Table(TABLE_NAME)

    # Fetch item by PhoneNumber
    response = table.get_item(Key={'PhoneNumber': phone_number})
    
    if 'Item' not in response:
        return {
            'statusCode': 400,
            'body': 'Phone number not found or OTP not requested.'
        }

    item = response['Item']
    stored_otp = item['OTP']
    expiry = item['ExpiryTime']
    current_time = int(time.time())

    if current_time > expiry:
        return {
            'statusCode': 400,
            'body': 'OTP has expired.'
        }

    if user_otp != stored_otp:
        return {
            'statusCode': 401,
            'body': 'Invalid OTP.'
        }

    return {
        'statusCode': 200,
        'body': 'OTP verified successfully!'
    }
