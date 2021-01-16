import requests
import sys
import random

phone = "15017662251"
path = sys.path[0]

# 手机UA
headers = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 MQQBrowser/10.1.1 Mobile/15E148 Safari/604.1 QBWebViewUA/2 QBWebViewType/1 WKType/1",
    "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; MI 8 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.8.14",
    "Mozilla/5.0 (Linux; U; Android 10; zh-CN; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.7.4.1054 Mobile Safari/537.36",
]

with open(r"{}\\smsAPI.txt".format(path), "r") as f:
    url_list = f.readlines()
    # print(url)

i = 0
for api in url_list:
    i = i + 1
    print("接口:{}".format(i))
    api_start = api.replace("\n", "").replace("[手机号码]", phone)
    # print(api)
    try:
        rasp = requests.get(api_start, headers={"User-Agent": str(random.choice(headers))}, timeout=20)
        print("响应", rasp.text)
        if rasp.status_code == 200:
            with open(r"{}\\200.txt".format(path), "a") as a:
                a.write(api)
    except Exception as e:
        print("发送错误,接口{}坏了".format(i), e)
    print("-----------------------------------------------")
