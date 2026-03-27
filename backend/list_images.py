import json
from boto3.dynamodb.conditions import Key
from db import table

def lambda_handler(event, context):
    try:
        params = event.get('queryStringParameters') or {}
        inspection_id = params.get('inspection_id')

        if not inspection_id:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"error": "inspection_id required"})
            }

        response = table.query(
            KeyConditionExpression=Key('PK').eq(inspection_id)
        )

        images = [
            item for item in response['Items']
            if item['SK'].startswith("IMAGE#")
        ]

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(images)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)})
        }