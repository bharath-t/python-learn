import boto3


def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': sum(1, 2)
    }


def d_sum(a, b):
    return a + b
