import json
import boto3
import os

def handler(event, context):
    s3 = boto3.client('s3')
    
    try:
        bucket_name = os.environ['S3_BUCKET_NAME']
        # Demo: Liệt kê các file trong S3
        response = s3.list_objects_v2(Bucket=bucket_name)
        file_names = [obj['Key'] for obj in response.get('Contents', [])]
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'status': 'Success',
                'version': '2.0',  
                'files_count': len(file_names),
                'files': file_names
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }