# 批量查詢同ip網站模塊
import requests
from lxml import etree
from fake_useragent import UserAgent
import sys
import re

# 获取脚本运行路径
path = sys.path[0]


# 查询ip
def sameIP(ip):
    global resp
    # 爬取站長之家工具
    url = "http://stool.chinaz.com/same"

    datafrom = {
        "s": str(ip),
        "page": ""
    }

    resp = requests.get(url=url, params=datafrom, headers={"User-Agent": str(UserAgent().random), })
    # print(resp.text)
    html = etree.HTML(resp.text)
    try:
        result = html.xpath("//div[@class='search-write-wrap w600 col-red lh30 fz14']")
        resultURL = result[0].text
        print(ip, resultURL)
    except:
        # resultURL = "有結果，請自行查看:" + str(resp.url)
        return "1"

    # <div class="search-write-wrap w600 col-red lh30 fz14">没有找到任何站点</div>


# 从文件读取ip
def readIP():
    global ipList
    with open(r"{}//result.txt".format(path), "r", encoding="utf8") as f:
        txt = f.readlines()

    # print(txt)

    ipList = []
    for line in txt:
        pat = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")
        ip = pat.findall(line)
        if ip == []:
            pass
        else:
            ip = ip[0]
            ipList.append(ip)


readIP()
for ip in ipList:
    res = sameIP(ip)
    if res == "1":
        print("有結果，請自行查看:" + str(resp.url))
    else:
        pass
