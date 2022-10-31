import re
import json
import logging
import boto3
from botocore.exceptions import ClientError
from datetime import datetime

bucket = 'log-generator-files-cs441'
key = 'logs/Log1.log' # 8mins, 02:11:00.063 - 02:19:32.061
time = '02:12:00'
delta = '3:00'
regex = '([a-c][e-g][0-3]|[A-Z][5-9][f-w]){5,15}'

# s3://log-generator-files-cs441/logs/LogFileGenerator.2022-09-20.log
# ([a-c][e-g][0-3]|[A-Z][5-9][f-w]){5,15}
# param1=val1&param2=val2


s3_client = boto3.client('s3')
res = s3_client.get_object(Bucket=bucket, Key=key)


resCode = res['ResponseMetadata']['HTTPStatusCode']
text = str(res['Body'].read())


# matches = re.search(r'\d{2}:\d{2}:\d{2}.\d{3}', str(res['Body'].read()))
matches = re.findall(r'(\d{2}:\d{2}:\d{2}.\d{3})', text)
# back = re.search(r'(\d{2}:\d{2}:\d{2}.\d{3})\D+\d{2}\D+$', text)

# print(text)
# print(matches.span())
print(matches[0][0:8])
print(matches[-1])

t1 = datetime.strptime(matches[0][0:8], "%H:%M:%S")
c2 = datetime.strptime(time, "%H:%M:%S")
datetime.strptime(time, "%H:%M:%S")



if (t1 > c2):
	print("Error: bad time match")
	exit(1)



# find the proper logs




# print(int(matches[0][0:8])) # +" "+int(time)+" "+int(matches[-1]))



# bucket = s3_client.Bucket('log-generator-files-cs441')





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
