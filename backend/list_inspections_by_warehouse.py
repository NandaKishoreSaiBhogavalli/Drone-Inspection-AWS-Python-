import json
from boto3.dynamodb.conditions import Key
from db import table

def lambda_handler(event, context):
    try:
        params = event.get('queryStringParameters') or {}
        warehouse_id = params.get('warehouse_id')

        if not warehouse_id:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"error": "warehouse_id required"})
            }

        response = table.query(
            KeyConditionExpression=Key('PK').eq(f"WAREHOUSE#{warehouse_id}")
        )

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(response['Items'])
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)})
        }