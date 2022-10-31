import requests
import yaml


with open('config.yml', 'r') as file:
	conf = yaml.safe_load(file)


response = requests.get(conf['url'] + "?t=" + conf['time'])


if(not response.json()):
	print("The time requested was not found in the logs")
	exit(0)



obj = {'t':conf['time'],'d':conf['delta'],'r':conf['regex'],'b':conf['bucket'],'k':conf['log']}
result = requests.post(conf['url'], json = obj)

print(result.json())

