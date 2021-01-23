'''
Author: whalefall
Date: 2021-01-23 10:55:21
LastEditors: whalefall
LastEditTime: 2021-01-23 10:57:28
Description: 已经过时了的【中国共青团为抗疫情向医护人鱼致敬活动】刷访客脚本,供[JS逆向思路]参考使用。
'''

import hashlib
import random
import threading
import time

import execjs
import requests
from fake_useragent import UserAgent

lock = threading.Lock()

appid = "12"
appsecret = "109743cc5aee57c0425c98b1ee01c1ea"


# 字符串转md5
def getStrAsMD5(parmStr):
    # 1、参数必须是utf8
    # 2、python3所有字符都是unicode形式，已经不存在unicode关键字
    # 3、python3 str 实质上就是unicode
    if isinstance(parmStr, str):
        # 如果是unicode先转utf-8
        parmStr = parmStr.encode("utf-8")
    m = hashlib.md5()
    m.update(parmStr)
    return m.hexdigest()


# 加个次数统计
i = 0


# OPQBOT发送好友信息
def send(content):
    url_send = "http://192.168.101.4:8888/v1/LuaApiCaller?qq=2593923636&funcname=SendMsg"
    datafrom = {
        "toUser": 2734184475,  # 发到哪个QQ或者群号
        "sendToType": 1,  # 自己选择对应会话的数值
        "sendMsgType": "TextMsg",
        "content": content,  # 要发送的文字内容
        "groupid": 0,  # 群号
    }
    try:
        resp = requests.post(url_send, json=datafrom)
        print("OPQBot返回:", resp.text)
    except Exception as e:
        print("OPQBot请求出错:", e)

# send("test")

def run(t_name):
    global i
    while True:
        # 获取秒级时间戳
        try:
            time_new = int(time.time())
            token = getStrAsMD5(appid + str(time_new) + appsecret)
            url = "http://app.southcn.com/weijiandu/flag.php"

            datafrom = {
                "user_name": "%E5%9B%BD%E5%BA%86",
                "time": time_new,
                "token": token,
            }
            resp = requests.post(url, data=datafrom, timeout=20)
            r2 = requests.post(url, data=datafrom, timeout=20).elapsed.total_seconds()
            r3 = requests.post(url, data=datafrom, timeout=20).elapsed.total_seconds()
            i = i + 3
            if i > 10000:
                i = 0  # 一开始首先 重置数据
                print(t_name, "达到条件发送QQ提醒并重置计数")
                c = "目前total:" + str(resp.json()["total"]) + " " + "网络延时:" + str(round(resp.elapsed.total_seconds(), 2)) + "s"
                print(c)
                send(c)

            total = round(float(float(resp.elapsed.total_seconds() + r2 + r3) / 3), 3)

            print(t_name + resp.text, "time:", total, "s", "请求次数:", i)
        except Exception as e:
            print(t_name, "出现错误", e)


if __name__ == "__main__":
    t1 = threading.Thread(target=run, args=("线程t1",))
    t2 = threading.Thread(target=run, args=("线程t2",))
    t3 = threading.Thread(target=run, args=("线程t3",))
    t4 = threading.Thread(target=run, args=("线程t4",))
    t5 = threading.Thread(target=run, args=("线程t5",))
    t6 = threading.Thread(target=run, args=("线程t6",))
    t7 = threading.Thread(target=run, args=("线程t7",))
    t8 = threading.Thread(target=run, args=("线程t8",))
    t9 = threading.Thread(target=run, args=("线程t9",))
    t10 = threading.Thread(target=run, args=("线程t10",))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()

    t11 = threading.Thread(target=run, args=("线程t11",))
    t12 = threading.Thread(target=run, args=("线程t12",))
    t13 = threading.Thread(target=run, args=("线程t13",))
    t14 = threading.Thread(target=run, args=("线程t14",))
    t15 = threading.Thread(target=run, args=("线程t15",))
    t16 = threading.Thread(target=run, args=("线程t16",))
    t17 = threading.Thread(target=run, args=("线程t17",))
    t18 = threading.Thread(target=run, args=("线程t18",))
    t19 = threading.Thread(target=run, args=("线程t19",))
    t20 = threading.Thread(target=run, args=("线程t20",))
    #
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()
    t17.start()
    t18.start()
    t19.start()
    t20.start()
