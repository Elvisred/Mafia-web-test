import json
import os


def handler():
    my_secret = os.environ.get('MY_SECRET')
    return {
            'statusCode': 200,
            'body': f'hello world! I have a {my_secret}'
            }
