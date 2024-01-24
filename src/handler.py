"""
dummy string
"""
import boto3


def lambda_handler(event, context):
    """
    dummy string
    """
    print(event, context)
    return {
        'statusCode': 200,
        'body': d_sum(1, 2)
    }


def d_sum(a, b):
    """
    dummy string
    """
    return a + b


def main():
    print('main executd')

