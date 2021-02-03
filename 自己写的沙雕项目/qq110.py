'''
Author: whalefall
Date: 2021-02-03 00:02:28
LastEditors: whalefall
LastEditTime: 2021-02-03 21:22:58
Description: 多线程请求`qq110.net`信誉查询平台 认真复习了一下多线程知识点
'''
import requests
from fake_useragent import UserAgent
import threading  # 多线程
import random


def qqID(content, qqID):
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Origin': 'http://qq110.net',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': str(UserAgent().random),
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': 'http://qq110.net/qq.php?wyCLP5qr',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    data = {
        'qq': str(qqID)
    }

    try:
        response = requests.post(
            'http://qq110.net/', headers=headers, data=data, verify=False)
        if str(response.status_code) == "200":
            print(" {} \033[1;30;42m{} {} \033[0m".format(
                content, response.url, response.status_code))
        else:
            print(content, response.url, response.status_code)

    except ConnectionError:
        print("\033[1;30;41m[Error]服务器连接超时!\033[0m")
    except Exception as e:
        print("\033[1;30;41m[Error]服务器未知错误!\033[0m", e)


def main(th):
    while True:
        qq = random.randint(1000000000, 9999999999)
        qqID("\033[1;30;44m 线程{} \033[0m".format(str(th)), qq)


# 敲黑板 多线程的实现方式
if __name__ == '__main__':
    threads = []
    thread_name = []
    for i in range(1, 257):
        thread_name.append(i)

    for name in thread_name:
        t = threading.Thread(target=main, args=(name,))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()
