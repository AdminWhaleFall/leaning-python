'''
Author: whalefall
Date: 2021-01-22 16:52:17
LastEditors: whalefall
LastEditTime: 2021-01-23 12:41:45
Description: 爬取百度疫情数据,并生成各种图表
'''
import json
import re
import sys

import requests

import matplotlib.pyplot as plt


path=sys.path[0]
url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner"
headers = {
    "User-Agent": "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
}

resp = requests.get(url, headers=headers).text

pat = re.compile(r'id="captain-config">(.*?)</script><script>')
# 替换一些东东
result = pat.findall(resp)[0].replace("(", "").replace(")", "").replace("'",'"')
# print(result)

# 将字符串转换为json
result = json.loads(result)
# print(result)

update_t=result["component"][0]["mapLastUpdatedTime"] # 数据更新时间
print(update_t)
# 国内数据列表
areaList=[] #储存地区
confirmedList=[] #储存累计确诊
caseList=result["component"][0]["caseList"]

# Todo:我想让他们从大到小排列诶 怎么实现
for provinces in caseList:
    area=provinces["area"] #地区
    confirmed=provinces["confirmed"] # 累计确诊
    # print(area,confirmed)
    areaList.append(area)
    confirmedList.append(confirmed)

# 数据可视化部分
fig=plt.figure()
ax=fig.add_subplot(111)
# ax.set(font="SimSun")
#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

ax.bar(areaList,confirmedList,color="lightblue",align="center")
plt.show()




