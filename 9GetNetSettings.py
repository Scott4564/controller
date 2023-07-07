import requests
import json

token = "NC-6-785f6d9d7a5d47da8f7e-nbi"
url = "http://127.0.0.1:58000/api/v1/wan/network-wide-setting"

# Request header
headers = {
      "X-Auth-Token": token,
      "Content-Type": "application/json"
}

# Request payload
payload = {}

# HTTP request
response = requests.request("GET", url, headers=headers, data=payload)

# Show results
print(response.status_code)
result = response.json()
print (json.dumps(result, indent=4))


