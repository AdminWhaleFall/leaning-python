'''
Author: whalefall
Date: 2021-01-22 16:52:17
LastEditors: whalefall
LastEditTime: 2021-01-22 17:38:16
Description: 爬取百度疫情数据
'''
import requests
import re
import json
import sys

path=sys.path[0]
url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner"
headers = {
    "User-Agent": "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
}

resp = requests.get(url, headers=headers).text.replace(" ", "")

pat = re.compile(r'id="captain-config">(.*?)</script><script>')
# 替换一些东东
result = pat.findall(resp)[0].replace("(", "").replace(")", "").replace("'",'"')
# print(result)

# 将字符串转换为json
result = json.loads(result)
# print(result)

with open(r"{}//疫情数据.json".format(path),"w",encoding="utf8") as f:
    f.write(str(result))
    print("写入成功!")

