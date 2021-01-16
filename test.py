# -*- coding: UTF-8 -*-
# pma宝塔漏洞扫描脚本 <仅供测试>
# 用nmap扫描网段内的888端口 保存在脚本目录下的pma.txt文件 扫描结果将保存在pmaResult.txt文件
# 扫描多了可能被机房屏蔽ip 可以直接加代理ip
from fake_useragent import UserAgent
import requests
import time
import sys

# 读取运行时的脚本绝对路径
path = sys.path[0]


# 读取pma.txt文件 提取ip保存到ipList
def readPma():
    with open(r"{}\pma.txt".format(path), "r") as f:
        ipList = f.readlines()


reselt = []


def requests():
    for i in range(0, len(ipList)):
        time.sleep(1)
        ip = ipList[i].replace("\n", "")
        url = "http://" + ip + "/pma/"
        try:
            resp = requests.get(url, headers={"User-Agent": UserAgent().random, }, timeout=8)
        except Exception as e:
            print(url, "请求失败")
            continue
        print(url, resp.status_code)
        if resp.status_code == 200:
            print("发现目标", url, resp.status_code)
            reselt.append(url)
        else:
            pass
        # time.sleep(10)


# 输出目标到文件
def output():
    for reseltIp in reselt:
        with open(r"{}\pmaResult.txt".format(path), "a") as p:
            p.write(reseltIp)
            print(reseltIp, "写入成功")


readPma()
requests()
output()
