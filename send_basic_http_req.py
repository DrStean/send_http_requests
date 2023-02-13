import requests
from datetime import datetime

proxies = {'https:': '<URL Proxy 1>', 'http': '<URL Proxy 2>'}
auth_base_url = '<Auth URL>'
auth_req_body = {'grant_type': 'password', 'client_id': '<client_id>', 'username': '<Username>', 'password': '<Password>', 'client_secret': '<Client Secret>'}
request_url = '<URL>'
proc_date = datetime.now()
#processed_date = proc_date.strftime("%c,%f")

auth_response = requests.post(auth_base_url, proxies=proxies, 
headers={'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}, data=auth_req_body)


# get the access_token
access_token = auth_response.json()["access_token"]


# Creating the next request
headers = {
   'Content-Type': 'application/json', 'Accept': 'application/json', "Authorization": f"Bearer {access_token}"
}

# Sending the request x times and print the header time and response body for each try
#for i in range(50): request_api = requests.get(request_url, proxies=proxies, headers=headers)
for i in range(500):
    response = requests.get(request_url, proxies=proxies, headers=headers)
    print(f"Request {i}, response: {response.text}\nResponse Header Date: {response.headers['Date']}")
