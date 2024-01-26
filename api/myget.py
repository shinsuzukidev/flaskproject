import requests

print("==================> script start")

post_url = "http://localhost:50001/user/sato"
print(requests.get(post_url).json())
print("==================> script end")

