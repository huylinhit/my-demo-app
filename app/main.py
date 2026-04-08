import json
import boto3
import os

def handler(event, context):
    # Lấy tên bucket từ Environment Variable cấu hình trên AWS Lambda
    bucket_name = os.environ.get('S3_BUCKET_NAME', 'my-demo-bucket')
    s3 = boto3.client('s3')
    
    try:
        # Demo: Liệt kê các file trong S3
        response = s3.list_objects_v2(Bucket=bucket_name)
        file_names = [obj['Key'] for obj in response.get('Contents', [])]
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'status': 'Success',
                'version': '2.0',  # Thay đổi version này để check CI/CD
                'files_count': len(file_names),
                'files': file_names
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }