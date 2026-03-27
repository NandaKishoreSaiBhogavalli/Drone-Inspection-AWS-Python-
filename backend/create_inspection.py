import json
from db import table
from utils import generate_id, current_time

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))

        warehouse_id = body.get('warehouse_id')
        drone_id = body.get('drone_id')

        if not warehouse_id or not drone_id:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"error": "warehouse_id and drone_id required"})
            }

        inspection_id = generate_id("INSPECTION")

        # Warehouse mapping
        table.put_item(Item={
            "PK": f"WAREHOUSE#{warehouse_id}",
            "SK": inspection_id,
            "drone_id": drone_id,
            "created_at": current_time()
        })

        # Drone mapping
        table.put_item(Item={
            "PK": f"DRONE#{drone_id}",
            "SK": inspection_id,
            "warehouse_id": warehouse_id
        })

        # Inspection metadata
        table.put_item(Item={
            "PK": inspection_id,
            "SK": "METADATA",
            "warehouse_id": warehouse_id,
            "drone_id": drone_id,
            "created_at": current_time()
        })

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"inspection_id": inspection_id})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)})
        }