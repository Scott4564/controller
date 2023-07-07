import requests
import json


url = "http://127.0.0.1:58000/api/v1/ticket"

# Request header
headers = {
  'Content-Type': 'application/json'
}

# Request payload
payload = json.dumps({
  "username": "admin",
  "password": "cisco123"
})

# HTTP request
response = requests.request("POST", url, headers=headers, data=payload)

# Find your token
result = response.json()
ticket = result["response"]["serviceTicket"]

# Show results
print(response.status_code)
print("Your token is: ", ticket)
