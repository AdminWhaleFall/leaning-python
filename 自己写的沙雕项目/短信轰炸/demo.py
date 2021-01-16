# 短信接口获取+验证
import requests
import random
from lxml import etree
import re
import time
import sys

# 轰炸平台
url_1 = "http://www.ydhz.xyz/"  # 云端轰炸
url_2 = "http://www.1314.buzz/"  # 污神轰炸
url_3 = "http://www.booms.ga/index.php?continue=null"  # BOOM轰炸 被佛山运营商劫持了 加 continue=null 参数即可
url_4 = "http://z.7qi.me/index.php?c=1"  # 在线短信测压
url_5 = "http://alhzj.xyz/"  # 阿狸轰炸

# 手机UA
headers = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 MQQBrowser/10.1.1 Mobile/15E148 Safari/604.1 QBWebViewUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; MI 8 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.8.14",
    "Mozilla/5.0 (Linux; U; Android 10; zh-CN; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.7.4.1054 Mobile Safari/537.36",
]


def getAPI(url_index, key):
    se = requests.session()
    se.get(url_index, headers={"User-Agent": str(random.choice(headers))})
    resp = se.get(url_index, params={key: "15017662289", "ok": ""}).text

    html = etree.HTML(resp)
    result = html.xpath("//img/@src")
    # print(result)

    url_list = []
    for url in result:
        url = url.replace(" ", "")
        # 匹配网址的正则表达式
        pat = re.compile(r"(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?")
        url_best = pat.search(url)

        if url_best == None:
            pass
        else:
            url_best = url_best.group().replace("15017662289", "[手机号码]")
            print(url_best)
            url_list.append(url_best)
    print(url_list)
    print("网址:{} 共获取到{}条接口".format(url_index, str(len(url_list))))
    return url_list


list_1 = getAPI(url_1, "hm")
# time.sleep(5)
list_2 = getAPI(url_2, "hm")
list_3 = getAPI(url_3, "hm")
list_4 = getAPI(url_4, "call")
list_5 = getAPI(url_5, "hm")

list_all = list_1 + list_2 + list_3 + list_4

list_new = []
for api in list_all:
    if api not in list_new:
        if "[手机号码]" in api:
            list_new.append(api)

print("查重\筛选 后接口数:{}".format(str(len(list_new))))

# 写入文件
path = sys.path[0]
for api_url in list_new:
    with open(r"{}\\smsAPI.txt".format(path), "a") as f:
        f.write(api_url + "\n")

print("写入成功")
