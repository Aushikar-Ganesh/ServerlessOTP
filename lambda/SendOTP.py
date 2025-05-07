import boto3
import random
import time
import os

# Initialize boto3 clients
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

# Environment variables
TABLE_NAME = os.environ['TABLE_NAME']
SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']

def lambda_handler(event, context):
    # Parse phone number from API call
    phone_number = event['queryStringParameters']['phone']

    # Generate a 6-digit random OTP
    otp = str(random.randint(100000, 999999))

    # Set expiry time (5 minutes from now)
    expiry_time = int(time.time()) + (5 * 60)

    # Save to DynamoDB
    table = dynamodb.Table(TABLE_NAME)
    table.put_item(
        Item={
            'PhoneNumber': phone_number,
            'OTP': otp,
            'ExpiryTime': expiry_time
        }
    )

    # Publish to SNS
    sns.publish(
    PhoneNumber=phone_number,
    Message=f'Your OTP is {otp}'
)

    return {
        'statusCode': 200,
        'body': f'OTP sent successfully to {phone_number}'
    }
