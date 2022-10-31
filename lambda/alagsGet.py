import json
import logging
import boto3
import re
from datetime import datetime

def lambda_handler(event, context):
    time = event["queryStringParameters"]["t"]
    buck = 'log-generator-files-cs441'
    keys = 'logs/Log1.log'
    v = False

    s3_client = boto3.client('s3')
    res = s3_client.get_object(Bucket=buck, Key=keys)

    resCode = res['ResponseMetadata']['HTTPStatusCode']
    text = str(res['Body'].read())

    matches = re.findall(r'(\d{2}:\d{2}:\d{2}.\d{3})', text)
    t1 = datetime.strptime(matches[0][0:8], "%H:%M:%S")
    c2 = datetime.strptime(time, "%H:%M:%S")

    if (t1 < c2):
        v = True

    return {
        'statusCode': 200,
        'body': json.dumps(v)
    }
