import json
from db import table

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))

        inspection_id = body.get('inspection_id')
        image_key = body.get('image_key')

        if not inspection_id or not image_key:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"error": "inspection_id and image_key required"})
            }

        table.put_item(
            Item={
                "PK": inspection_id,
                "SK": f"IMAGE#{image_key}",
                "image_url": image_key
            },
            ConditionExpression="attribute_not_exists(SK)"
        )

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "Image saved"})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)})
        }