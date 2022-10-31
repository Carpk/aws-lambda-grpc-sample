import json
import logging
import boto3
import re
from datetime import datetime

def lambda_handler(event, context):

    s3_client = boto3.client('s3')
    res = s3_client.get_object(Bucket='log-generator-files-cs441', Key='logs/Log1.log')

    resCode = res['ResponseMetadata']['HTTPStatusCode']

    text = str(res['Body'].read())
    matches = re.findall(r'(\d{2}:\d{2}:\d{2}.\d{3})', text)

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }