'''
Author: WhaleFall
Date: 2021-01-24 10:44:04
LastEditTime: 2021-01-24 13:27:40
Description: 获取Github服务器实时ip地址,并写入hosts文件,国内github服务器dns污染严重只能这样了。
ps: 除此之外, "科学上网" 或许是最直接有效方式.
'''
import requests
from lxml import etree
import time
import re
import sys
# 在控制台显示绚丽的色彩Windows平台
# import colorama
# from colorama import init, Fore, Back, Style
# init(autoreset=True)

# 从https://www.ipaddress.com获取最新的ip地址

# 所有github服务的域名

urlist = [
    "github.com",
    "nodeload.github.com",
    "api.github.com",
    "training.github.com",
    "codeload.github.com",
    "assets-cdn.github.com",
    "documentcloud.github.com",
    "help.github.com",
    "githubstatus.com",
    "github.global.ssl.fastly.net",
    "raw.github.com",
    "raw.githubusercontent.com",
    "cloud.githubusercontent.com",
    "gist.githubusercontent.com",
    "marketplace-screenshots.githubusercontent.com",
    "repository-images.githubusercontent.com",
    "user-images.githubusercontent.com",
    "desktop.githubusercontent.com",
    "avatars0.githubusercontent.com",
    "avatars1.githubusercontent.com",
    "avatars2.githubusercontent.com",
    "avatars3.githubusercontent.com",
    "avatars4.githubusercontent.com",
    "avatars5.githubusercontent.com",
    "avatars6.githubusercontent.com",
    "avatars7.githubusercontent.com",
    "avatars8.githubusercontent.com",
]


# 三级域名的处理 输出查询地址
def checkUrl(url):
    # 正则表达式渣渣,换另一个思路叭
    # pat=re.compile(r"\w.\w+")
    # result=pat.findall(url)
    # print(result)
    url_sp = url.split(".")
    # 根域名
    url_root = url_sp[len(url_sp) - 2] + "." + url_sp[len(url_sp) - 1]

    # 判断
    if len(url_sp) == 2:
        get_url = "https://" + str(url_root) + ".ipaddress.com"
    else:
        get_url = "https://" + str(url_root) + ".ipaddress.com/" + url

    # print(get_url)

    return get_url


# checkUrl("avatars7.githubusercontent.com")


def getAddress(get_url, start_url):
    header = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    }

    resp = requests.get(get_url, headers=header).text
    # print(resp)
    html = etree.HTML(resp)
    # 浏览器控制台会自己加上/tbody/要删除  text()获取里面的文本
    # <ul class="comma-separated"><li>39.156.69.79</li><li>220.181.38.148</li></ul>
    # /html/body/div/main/section[1]/table/tbody/tr[2]/td/ul
    # /html/body/div[1]/main/section[1]/table/tr[6]/td/ul//text()
    result = html.xpath(r'//td//ul//text()')

    resList = []
    # 拿到结果还要筛选出ip地址
    for result in result:
        # print(result)
        pat = re.compile(
            r"((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}"
        )
        res = pat.search(result)
        if res == None:
            continue
        else:
            # print(res.group())
            resList.append(res.group())

    # 列表去重
    resList = list(set(resList))
    result = resList

    if result == []:
        print(r"[Error]获取IP失败 网站:{}".format(start_url))
        return "0"
    else:

        print(r"网站:{} ip地址:{}".format(start_url, result))
        # 默认取第一个ip
        return result[0]


# getAddress("baidu.com")

# 遍历获取ip
for url in urlist:
    url_get = checkUrl(url)
    ipAddress = getAddress(url_get, url)
    # time.sleep(10)
    with open(r"{}//githubHosts.txt".format(sys.path[0]), "a") as f:
        f.write("{} {}\r".format(str(url), str(ipAddress)))

print("已在脚本目录生成 githubHost.txt文件 将其内容追加到系统host文件即可!")
