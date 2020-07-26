import requests

url = "https://ios-xe-mgmt-latest.cisco.com:9443/restconf/data/Cisco-IOS-XE-native:native?content=config"

payload = {}
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic ################'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
