import requests
import json


url = "http://127.0.0.1:58000/api/v1/user/role"

# Request header
headers = {}

# Request payload
payload = {}

# HTTP request
response = requests.request("GET", url, headers=headers, data=payload)

# Find your token
#result = response.json()

# Show results
print(response.status_code)
print(response.text)
