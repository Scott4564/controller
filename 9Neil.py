import requests
import json

token = "NC-6-785f6d9d7a5d47da8f7e-nbi"
url = "http://127.0.0.1:58000/api/v1/wan/network-wide-setting"

# Request header
headers = {
      "X-Auth-Token": token,
      "Content-Type": "application/json"
}

data = json.dumps({
    "syslog" : [
        {"serverIp": "192.168.100.200"},
        {"serverIp": "33.33.33.33"},
    ]
})
resp = requests.request("POST", url+"/wan/network-wide-setting", headers=headers, data=data)

print (resp.status_code)
result = resp.json()
print (json.dumps(result, indent=4))
