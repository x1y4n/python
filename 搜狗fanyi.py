import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36"
    }
data = {"from": "auto",
        "to": "zh-CHS",
        "client": "wap",
        "text": input(),
        "uuid": "b524d06c-156a-423a-911d-1d4c1dd5c896",
        "pid": "sogou-dict-vr",
        "addSugg": "on"
        }
post_url = " https://fanyi.sogou.com/reventondc/suggV3"
response = requests.post(post_url, data=data, headers=headers)
# print(response.content.decode())
dict = json.loads(response.content.decode())
print(response.json())
print(dict)
print(response.content.decode())
try:
    ret = dict["sugg"][0]["v"]
    print(ret)

except:
    print(dict["message"])
    KeyError
