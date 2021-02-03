'''
Author: whalefall
Date: 2021-02-03 00:02:28
LastEditors: whalefall
LastEditTime: 2021-02-03 09:34:16
Description: file content
'''
import requests
from fake_useragent import UserAgent
import threading  # 多线程
import random


def qqID(content,qqID):
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

    response = requests.post(
        'http://qq110.net/', headers=headers, data=data, verify=False)

    print(content,response.url, qqID)


def main(th):
    while True:
        qq = random.randint(2734184475,9999999999)
        qqID("线程{}".format(str(th)), qq)


# 敲黑板 多线程的实现方式
if __name__ == '__main__':
    threads = []
    thread_name = []
    for i in range(1,129):
        thread_name.append(i)
    
    for name in thread_name:
        t = threading.Thread(target=main, args=(name,))
        t.start()
        threads.append(t)
        
    for thread in threads:
        thread.join()
