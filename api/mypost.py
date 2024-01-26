import requests
import json

print("==================> script start")

post_url = "http://localhost:50001/regist_user"
json = { "name": "sato"}

resp = requests.post(
    post_url,
    json = json
  )

print(resp.json())
print("==================> script end")

