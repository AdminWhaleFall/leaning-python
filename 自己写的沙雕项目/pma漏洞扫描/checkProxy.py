import requests
import sys
from fake_useragent import UserAgent
# 导入大佬写的获取免费可用代理模块
from http_Proxy import get_proxy
import random
import re

# 获取脚本路径
path = sys.path[0]


def getProxy():
    # 调用获取代理ip并写入文件
    HttpProxyList = get_proxy("http", 8)

    HttpProxyList = str(HttpProxyList)
    print("获取到的http代理:\n", HttpProxyList)
    with open(r"{}\httpProxy.txt".format(path), "a") as f1:
        f1.write(HttpProxyList)

    HttpsProxyList = get_proxy("https", 8)
    HttpsProxyList = str(HttpsProxyList)
    print("获取到的https代理:\n", HttpsProxyList)
    with open(r"{}\httpsProxy.txt".format(path), "a") as f2:
        f2.write(HttpsProxyList)


# 检验代理ip地区
def CheckHttpWhele(HttpProxyIp):
    # 可以正则匹配一下HttpProxyIp里边的ip地址
    pat = re.compile(r"(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])")
    HttpProxyIp = pat.search(HttpProxyIp).group()

    # 调用ip.cn获取ip地址 不需要用代理ip访问
    url_whare = "http://whois.pconline.com.cn/ip.jsp?ip={}".format(str(HttpProxyIp))
    try:
        resp = requests.get(url_whare, headers={"User-Agent": str(UserAgent().random)})
        # 替换掉 空格 换行 回车
        whare = resp.text.replace("\n", "").replace("\r", "").replace(" ", "")
        # print(whare)
        return whare
    except Exception as e:
        print("未知原因的请求失败", str(e))
        return "0"


# 读取文件转换为列表
def ReadIpList():
    # 读取http文件
    with open("{}//httpProxy.txt".format(path), "r") as http:
        httpList = http.readlines()[0]
    # 读取https文件
    with open("{}//httpsProxy.txt".format(path), "r") as http:
        httpsList = http.readlines()[0]

    # 看来要正则匹配''里边的东西了
    pat = re.compile(r"'(.*?)'")
    httpList = pat.findall(httpList)
    httpsList = pat.findall(httpsList)

    return httpList, httpsList


# 测试http请求延时 请求百度
def CheckHttpTime(ProxyIp, proxy_type):
    if proxy_type == "http":
        url = "http://baidu.com/"
    elif proxy_type == "https":
        url = "https://baidu.com/"
    else:
        print("请求类型错误")
        return "0"
    try:
        # proxies会根据请求的url协议自动选择
        resp = requests.get(url, headers={"User-Agent": str(UserAgent().random)},
                            proxies={"https": "https://{}".format(ProxyIp), "http": "http://{}".format(ProxyIp)},
                            timeout=8)
        # 获取请求时间 单位s 保留两位小数
        result = str(round(resp.elapsed.total_seconds(), 2)) + "s"
    except Exception as e:
        result = "-0s" + " " + "请求失败"
    # print(result)
    return result


# getProxy()

# 读取文件并储存在列表里边
httpList, httpsList = ReadIpList()
print("从文件读取完成")
# 检测http代理
resultHttp = ""
print("检测http代理")
for httpIP in httpList:
    print("--------------------------------------")
    whale = CheckHttpWhele(httpIP)
    outtime = CheckHttpTime(httpIP, "http")
    print(httpIP + " " + "地区:" + whale + " " + "延时:" + outtime)
    resultHttp = "------------------------------------\n" + httpIP + " " + "地区:" + whale + " " + "延时:" + outtime + "\n" + resultHttp

# 检测https代理
print("检测https代理")
resultHttps = ""
for httpsIP in httpsList:
    print("--------------------------------------")
    whale = CheckHttpWhele(httpsIP)
    outtime = CheckHttpTime(httpsIP, "https")
    print(httpIP + " " + "地区:" + whale + " " + "延时:" + outtime)
    resultHttps = "------------------------------------\n" + httpsIP + " " + "地区:" + whale + " " + "延时:" + outtime + "\n" + resultHttps

with open("{}//CheckProxyResult.txt".format(path), "w") as r:
    r.write(">>http代理:<<" + "\n" + resultHttp + "\n" + ">>https代理<<" + "\n" + resultHttps)
