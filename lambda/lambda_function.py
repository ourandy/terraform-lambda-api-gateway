import requests
import json

def lambda_handler():
    r = requests.get("https://api.github.com")
    user = r.json()['current_user_url']
    return {
        "statusCode": 200,
        "body": json.dumps({"user": user}),
        "headers": {"Content-Type": "application/json"}
    }
