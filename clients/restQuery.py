import requests
import yaml


with open('config.yml', 'r') as file:
	conf = yaml.safe_load(file)


print(conf['url'])

url = "https://hz7xtzk10h.execute-api.us-east-1.amazonaws.com/Prod/alags/"


response = requests.get(conf['url'] + "?t=" + conf['time'])

print(response.json())






# session = requests.Session()

# # url = "https://hz7xtzk10h.execute-api.us-east-1.amazonaws.com/Prod/alags/?t=10:00"
# # # credentials = {"userName": "administrator", "password": "adminpass"}
# # headers = {"accept": "application/json",
# #            "content-type": "application/json",
# #            "x-api-version": "120"
# #           }

# # response = session.post(url, headers=headers, verify=False)

# # session_id = response.json()["sessionID"]

# url = "https://hz7xtzk10h.execute-api.us-east-1.amazonaws.com/Prod/alags/?t=10:00"
# headers = {"accept": "application/json",
#            "content-type": "text/csv",
#            "x-api-version": "2"
#           }

# response = session.get(url, headers=headers, verify=False)

# print(response)



