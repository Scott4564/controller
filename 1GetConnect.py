import requests

url = "http://127.0.0.1:58000"

# Request header
headers = {}
# Request payload
payload = ""
# HTTP request
response = requests.request("GET", url, headers=headers, data=payload)

# Show results
print(response.status_code)
