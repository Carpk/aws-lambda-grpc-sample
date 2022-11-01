import json
import logging
import boto3
import re
from botocore.exceptions import ClientError
from datetime import datetime, timedelta

def lambda_handler(event, context):
    obj = json.loads(event.get('body', None))
    time = obj['t']
    delta = obj['d']
    regex = obj['r']
    bucket = obj['b']
    key = obj['k']

    s3_client = boto3.client('s3')
    res = s3_client.get_object(Bucket=bucket, Key=key)
    searchTime = datetime.strptime(time, "%H:%M:%S")

    resCode = res['ResponseMetadata']['HTTPStatusCode']

    text = str(res['Body'].read().decode('utf-8'))
    txtArry = text.splitlines()

    while (txtArry[0][0] == '['):
        txtArry.pop(0)

    size = len(txtArry)

    while (txtArry[size-1][0] == '['):
        txtArry.pop(size-1)
        size = len(txtArry)

    first = 0
    last = size

    while(last-first > 1):
        size = last-first # 12 - 4
        half = int((size)/2) + first
        midTime = datetime.strptime(txtArry[half][0:8], "%H:%M:%S")

        if (searchTime == midTime):
            break
        elif (searchTime < midTime):
            last = half
        elif (midTime < searchTime):
            first = half

    currTime = datetime.strptime(txtArry[first][0:8], "%H:%M:%S")
    endTime = currTime + timedelta(minutes=int(delta[0:2]), seconds=int(delta[3:5]))
    endArray = len(txtArry)
    final = []

    while ((first < endArray) & (currTime < endTime)):
        data = txtArry[first].split(" ")[-1]
        matchdata = re.search(regex, data)
        if(matchdata):
            final.append(data)
        first += 1
        currTime = datetime.strptime(txtArry[first][0:8], "%H:%M:%S")

    return {
        'statusCode': 200,
        'body': json.dumps(final)
    }
