import requests

# session = requests.Session()

url = "https://hz7xtzk10h.execute-api.us-east-1.amazonaws.com/Prod/alags/"


response = requests.get(url+"?t=10:52")
print(response.json())







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




