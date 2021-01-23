'''
Author: whalefall
Date: 2021-01-23 11:06:51
LastEditors: whalefall
LastEditTime: 2021-01-23 11:07:32
Description: 爬取随机妹子图api 应该不能用了叭
'''

import random
import sys

import requests
from fake_useragent import UserAgent

# 随机图片api爬取
path = sys.path[0]


def dowload(time):
    global path
    url = "https://work.dxinj.com/hea/api.php"
    resp = requests.get(url, headers={"User-Agent": str(UserAgent().random)}).content
    print("请求次数 {} ".format(time))
    # with open(r"{}//laopo//{}.jpg".format(path, str(time)), "wb") as f:
    #     f.write(resp)
    #     print("{}.jpg 下载完成".format(time))


for i in range(1, 999999):
    dowload(i)
