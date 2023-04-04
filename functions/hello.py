import json

def handler(event, context):
    body = {
        "message": "Hello from Netlify Functions!"
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
