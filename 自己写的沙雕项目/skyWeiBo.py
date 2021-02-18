'''
Author: your name
Date: 2021-02-12 10:55:19
LastEditTime: 2021-02-12 18:52:36
LastEditors: Please set LastEditors
Description: In User Settings Edit
'''
import requests
url = "https://m.weibo.cn/api/container/getIndex?type=uid&value=6355968578&containerid=1076036355968578"
header = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36",
}
resp = requests.get(url, headers=header).json()

content = resp["data"]["cards"][0]["mblog"]["raw_text"]
# data.cards[1].mblog.raw_text
print(content)
