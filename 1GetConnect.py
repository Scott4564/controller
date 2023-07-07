import requests

url = "http://127.0.0.1:58000"

# Request header
headers = {}
# Request payload
payload = ""
# HTTP request
response = requests.request("GET", url, headers=headers, data=payload)

# Show status
print(response.status_code)
# Show response header
print(response.headers)
# Show results
print(response.json())

# Close connection
response.close()