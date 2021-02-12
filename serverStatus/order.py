'''
Author: whalefall
Date: 2021-02-08 10:16:37
LastEditors: whalefall
LastEditTime: 2021-02-08 17:17:03
Description: ServerStatus|其他模块函数文件|树莓派推送测试
'''
import requests
import random

# 检查网络连接


def checkNetwork():
    urlList = ["https://baidu.com", "https://bing.cn", "https://zhihu.com"]
    url = random.choice(urlList)
    try:
        resp = requests.get(url, headers={
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"})
    except requests.exceptions.ConnectionError:
        print("[Error]网络连接异常!")
        return "Error"
    except Exception as e:
        print("[Error]网络连接异常!",e)
        return "Error"
    else:
        if str(resp.status_code)=="200":
            print("[Suc]网络正常")
            return "Success"
        else:
            print("[Suc]网络正常,但请求出现错误!")
            return "Success"

# 获取系统具体状态
def getSystemStatus():


checkNetwork()
