import re
import json
import logging
import boto3
from botocore.exceptions import ClientError
from datetime import datetime, timedelta
# from datetime import timedelta

bucket = 'log-generator-files-cs441'
key = 'logs/Log1.log' # 8mins, 02:11:00.063 - 02:19:32.061
time = '02:12:00'
delta = '06:00'
regex = '([a-c][e-g][0-3]|[A-Z][5-9][f-w]){5,15}'


################################### GET ###################################

# param1=val1&param2=val2

s3_client = boto3.client('s3')
res = s3_client.get_object(Bucket=bucket, Key=key)


resCode = res['ResponseMetadata']['HTTPStatusCode']
text = str(res['Body'].read().decode('utf-8'))


# matches = re.search(r'\d{2}:\d{2}:\d{2}.\d{3}', str(res['Body'].read()))
matches = re.findall(r'(\d{2}:\d{2}:\d{2}.\d{3})', text)
# back = re.search(r'(\d{2}:\d{2}:\d{2}.\d{3})\D+\d{2}\D+$', text)

# print(text)
# print(matches.span())
print(matches[0][0:8])
print(matches[-1])

t1 = datetime.strptime(matches[0][0:8], "%H:%M:%S")
searchTime = datetime.strptime(time, "%H:%M:%S")
datetime.strptime(time, "%H:%M:%S")


if (t1 > searchTime):
	print("Error: bad time match")
	exit(1)


################################### POST ###################################
# find the proper logs

print("in POST")

txtArry = text.splitlines()


while (txtArry[0][0] == '['):
	# print("front popping: " + txtArry[0][0])
	txtArry.pop(0)

size = len(txtArry)

while (txtArry[size-1][0] == '['):
	# print("back popping: " + txtArry[size-1][0])
	txtArry.pop(size-1)
	size = len(txtArry)


first = 0
last = size


while(last-first > 1):
	size = last-first # 12 - 4
	half = int((size)/2) + first

	# print(str(first)+" < "+str(half+first)+" < "+str(last))

	midTime = datetime.strptime(txtArry[half][0:8], "%H:%M:%S")

	if (searchTime == midTime):
		break
	elif (searchTime < midTime):
		last = half
	elif (midTime < searchTime):
		first = half


print("first: " + txtArry[first])


currTime = datetime.strptime(txtArry[first][0:8], "%H:%M:%S")
endTime = currTime + timedelta(minutes=int(delta[0:2]), seconds=int(delta[3:5]))
endArray = len(txtArry)
final = []
# print(delta[0:2])
# print(delta[3:5])
# print(timedelta(minutes=int(delta[0:2]), seconds=int(delta[3:5])))
# print(endTime)
while ((first < endArray) & (currTime < endTime)):
	data = txtArry[first].split(" ")[-1]
	matchdata = re.search(regex, data)
	if(matchdata):
		final.append(data)
	# print(matchdata)

	first += 1
	currTime = datetime.strptime(txtArry[first][0:8], "%H:%M:%S")



print(final)



# while(size>2):
# 	size = len(txtArry)
# 	half = int(size/2)
# 	print(txtArry[half])
# 	midTime = datetime.strptime(txtArry[half][0:8], "%H:%M:%S")
# 	# if ():
# 	if(midTime > searchTime):
# 		txtArry = txtArry[0:half]
# 	if (midTime < searchTime):
# 		txtArry = txtArry[half:size]





# print(txtArry)


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
