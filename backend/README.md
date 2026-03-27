📌 Project: Drone Inspection Backend

🚀 Tech Stack
- AWS Lambda
- API Gateway (HTTP API)
- DynamoDB
- S3 (for image storage)

📌 APIs Implemented
1.Create Inspection
- POST /inspection
2.List Inspections by Warehouse
- GET /inspection/warehouse?warehouse_id=1
3.List Inspections by Drone
- GET /inspection/drone?drone_id=D1
4.Generate Upload URL
- GET /inspection/upload-url
5.Save Image
- POST /inspection/image
6.List Images
- GET /inspection/images

📌 Note
Due to time constraints, minor integration issues may exist, but:
-Architecture is fully designed
-All endpoints implemented
-DynamoDB schema correctly structured