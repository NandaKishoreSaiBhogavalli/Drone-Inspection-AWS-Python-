import boto3
import json
import uuid

s3 = boto3.client('s3')
BUCKET = "drone-inspection-images-madhu"

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

        image_id = str(uuid.uuid4())
        key = f"{inspection_id}/{image_id}.jpg"

        url = s3.generate_presigned_url(
            'put_object',
            Params={
                'Bucket': BUCKET,
                'Key': key
            },
            ExpiresIn=3600
        )

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "upload_url": url,
                "image_key": key
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)})
        }