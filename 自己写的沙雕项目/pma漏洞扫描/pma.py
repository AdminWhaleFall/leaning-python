'''
Author: whalefall
Date: 2021-01-23 11:04:07
LastEditors: whalefall
LastEditTime: 2021-01-23 11:05:48
Description: 之前写的宝塔便班pma漏洞扫描程序,已经开源到gitee上面了,github再备份一下叭
'''

# -*- coding: UTF-8 -*-
# pma宝塔漏洞扫描脚本 <仅供测试>
# 作者：落落 telegramID:whalefall9420

'''
用nmap扫描网段内的888端口 保存在脚本目录下的pma.txt文件 扫描结果将保存在pmaResult.txt文件
扫描多了可能被机房屏蔽ip 可以直接加代理ip
需要安装的模块
pip install fake_useragent
pip install requests
用法:
1.先找到 ip网段 https://blog.csdn.net/nxuu01/article/details/102779652
2.用nmap扫描该网段开放的888端口保存在pma.txt文件 格式要求：ip:port
nmap -vv -n --open -p 888 网段 | awk -F'[ /]' '/Discovered open port/{print $NF":"$4}' >> pma.txt

'''

from fake_useragent import UserAgent
import requests
import time
import sys
from http_Proxy import get_proxy

# 读取运行时的脚本绝对路径
path = sys.path[0]


# 读取pma.txt文件 提取ip保存到ipList
def readPma():
    global ipList
    with open(r"{}\pmabate.txt".format(path), "r") as f:
        ipList = f.readlines()


reselt = []


def request():
    global reselt
    for i in range(0, len(ipList)):
        # time.sleep(0.5)
        ip = ipList[i].replace("\n", "")
        url = "http://" + ip + ":80/phpmyadmin"
        try:
            resp = requests.get(url, headers={"User-Agent": str(UserAgent().random)}, timeout=1)
        except Exception as e:
            print(url, "请求失败", e)
            continue

        print(url, resp.status_code)

        if resp.status_code == 200:
            print("发现目标", url, resp.status_code)
            # print(resp.text)
            # print("--------------------------------")
            reselt.append(url)
        if resp.status_code == 404:
            pass
        else:
            pass


# 输出目标到文件
def output():
    for reseltIp in reselt:
        with open(r"{}\bateResult.txt".format(path), "a") as p:
            p.write(reseltIp)
            print(reseltIp, "写入成功")


readPma()
request()
output()

# 获取代理ip并写入文件
# proxyList = get_proxy("http", 8)
# # proxyList=['196.53.119.111:80', '105.27.238.161:80', '14.187.137.54:10003', '101.37.118.54:8888', '105.27.237.24:80', '195.182.152.238:38178', '201.217.4.101:53281', '196.53.119.32:80', '105.27.237.31:80', '176.101.89.226:33470', '186.225.110.166:8080', '105.27.238.164:80', '177.184.148.246:8080', '196.53.88.117:80', '105.27.237.27:80', '77.232.167.200:47211', '117.66.148.178:3000', '14.207.145.80:8080', '211.137.52.158:8080', '105.27.238.166:80', '14.207.78.71:8080', '200.52.77.36:80', '118.173.232.61:47115', '221.180.170.104:8080', '105.27.238.162:80', '105.27.238.160:80', '180.183.101.178:8080', '80.241.222.138:80', '3.10.145.250:80', '91.205.174.26:80', '183.89.170.119:8080', '107.178.6.30:8080', '45.133.182.18:18080', '197.248.184.158:53281', '196.53.116.118:80', '110.78.182.75:8080', '105.27.237.30:80', '105.27.238.163:80', '203.99.133.30:80', '118.175.93.94:45175']
# ipList = str(proxyList)
# # for ip in proxyList:
# #     with open(r"{}\httpsProxy.txt".format(path), "a") as p:
# #         p.write(ip+"\n")
# #         print(ip, "写入成功")
# with open(r"{}\httpProxyNew.txt".format(path), "a") as p:
#     p.write(ipList)
