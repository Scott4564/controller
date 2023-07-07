import requests
import json
import apiToken

token = "NC-6-785f6d9d7a5d47da8f7e-nbi"
url = "http://127.0.0.1:58000/api/v1/wan/network-wide-setting"    #wan/network-wide-setting"

# Request header
headers = {
      "X-Auth-Token": apiToken.API_TOKEN,
      "Content-Type": "application/json"
}

# Request payload
payload = json.dumps({
    "syslog" : [
        {"serverIp": "192.168.100.200"},
        {"serverIp": "33.33.33.33"},
    ],
      "ntp": {"serverIp": "192.168.100.250"},
      "dns": {"name": "ensa.com",
              "ipAddress": "192.168.100.100"}
})


# HTTP request
response = requests.request("PUT", url, headers=headers, data=payload)

# Show status
print(response.status_code)
# Show response header
print(response.headers)
# Show results
result = response.json()
print (json.dumps(result, indent=4))


