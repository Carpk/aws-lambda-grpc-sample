import re
import json
import logging
import boto3
from datetime import datetime, timedelta


bucket = 'log-generator-files-cs441'
key = 'logs/Log1.log' # 8 mins, 02:11:00.063 - 02:19:32.061
time = '02:12:00'
delta = '06:00'
regex = '([a-c][e-g][0-3]|[A-Z][5-9][f-w]){5,15}'


def getData():
	s3_client = boto3.client('s3')
	res = s3_client.get_object(Bucket=bucket, Key=key)
	s3_client.close()
	return res['Body'].read().decode('utf-8')


def findTimePeriod(text):
	return re.findall(r'(\d{2}:\d{2}:\d{2}.\d{3})', text)
	# [match[0],match[-1]] or tuple



def datetime_convert(time):
	# t1 = datetime.strptime(matches[0][0:8], "%H:%M:%S")
	return datetime.strptime(time, "%H:%M:%S")


def is_in_range(start, search):
	return search > start


# txtArry = text.splitlines()


def remove_front_nonlog(textArry):
	while (textArry[0][0] == '['):
		textArry.pop(0)
	return textArry



# while (txtArry[size-1][0] == '['):
# 	# print("back popping: " + txtArry[size-1][0])
# 	txtArry.pop(size-1)
# 	size = len(txtArry)


# first = 0
# last = size


# while(last-first > 1):
# 	size = last-first # 12 - 4
# 	half = int((size)/2) + first

# 	# print(str(first)+" < "+str(half+first)+" < "+str(last))

# 	midTime = datetime.strptime(txtArry[half][0:8], "%H:%M:%S")

# 	if (searchTime == midTime):
# 		break
# 	elif (searchTime < midTime):
# 		last = half
# 	elif (midTime < searchTime):
# 		first = half


# print("first: " + txtArry[first])


# currTime = datetime.strptime(txtArry[first][0:8], "%H:%M:%S")
# endTime = currTime + timedelta(minutes=int(delta[0:2]), seconds=int(delta[3:5]))
# endArray = len(txtArry)
# final = []
# # print(delta[0:2])
# # print(delta[3:5])
# # print(timedelta(minutes=int(delta[0:2]), seconds=int(delta[3:5])))
# # print(endTime)
# while ((first < endArray) & (currTime < endTime)):
# 	data = txtArry[first].split(" ")[-1]
# 	matchdata = re.search(regex, data)
# 	if(matchdata):
# 		final.append(data)
# 	# print(matchdata)

# 	first += 1
# 	currTime = datetime.strptime(txtArry[first][0:8], "%H:%M:%S")



# print(final)