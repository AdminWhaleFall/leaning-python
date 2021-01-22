'''
Author: whalefall
Date: 2021-01-22 15:42:48
LastEditTime: 2021-01-22 15:48:25
LastEditors: Please set LastEditors
Description: 弄一下腾讯课堂,看看有没有什么好玩的东西
'''
import requests
from fake_useragent import UserAgent

# 上课链接
url = "https://ke.qq.com/webcourse/486386/100583267#from=800021724&lite=1"

resp = requests.get(url,headers={"User-Agent": str(UserAgent())})

print(resp.text)