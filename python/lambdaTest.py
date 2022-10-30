import re
import json
import logging
import boto3
from botocore.exceptions import ClientError


# log-generator-files-cs441
# s3://log-generator-files-cs441/logs/LogFileGenerator.2022-09-20.log
# ([a-c][e-g][0-3]|[A-Z][5-9][f-w]){5,15}

# try:
s3_client = boto3.client('s3')
# bucket = s3_client.Bucket('log-generator-files-cs441')
res = s3_client.get_object(Bucket='log-generator-files-cs441', Key='logs/Log1.log')

# except ClientError as e:
#     logging.error(e)

resCode = res['ResponseMetadata']['HTTPStatusCode']

text = str(res['Body'].read())

# matches = re.search(r'\d{2}:\d{2}:\d{2}.\d{3}', str(res['Body'].read()))
matches = re.findall(r'(\d{2}:\d{2}:\d{2}.\d{3})', text)
# back = re.search(r'(\d{2}:\d{2}:\d{2}.\d{3})\D+\d{2}\D+$', text)




# print(text)
# print(matches.span())
print(matches[0])
print(matches[-1])















# {
# 	"Version": "2012-10-17",
# 	"Id": "Policy1667053611080",
# 	"Statement": [
# 		{
# 			"Sid": "Stmt1667053365686",
# 			"Effect": "Allow",
# 			"Principal": "*",
# 			"Action": "s3:GetObject",
# 			"Resource": "arn:aws:s3:::log-generator-files-cs441/logs/"
# 		}
# 	]
# }
