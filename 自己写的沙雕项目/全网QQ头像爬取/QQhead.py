'''
Author: whalefall
Date: 2021-01-22 14:42:59
LastEditors: whalefall
LastEditTime: 2021-01-23 08:48:22
Description: 生成随机QQ号并获取他的昵称和头像,存入数据库或下载到../img文件夹(然而没什么卵用)
'''

# todo:目前没时间完善了,有时间再修改叭

# coding=utf-8

import requests
import re
import hashlib
import sys
import random
import time
import threading

path = sys.path[0]

header = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 5X Build/OPM1.171019.019; wv) \
    AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser\
    /6.2 TBS/045120 Mobile Safari/537.36 V1_AND_SQ_8.2.7_1334_YYB_D QQ/8.2.7.4410 NetType\
    /WIFI WebP/0.3.0 Pixel/1080 StatusBarHeight/72 SimpleUISwitch/0"
}


# 获取到的图片二进制信息转md5
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


# 文件名去除非法字符
def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title


def getHead():
    global name
    global qqID
    url = "https://r.qzone.qq.com/fcg-bin/cgi_get_portrait.fcg?uins=" + \
        str(qqID)
    try:
        resp = requests.get(url, headers=header).content.decode(encoding="gbk")
    except Exception as e:
        print("可能是编码错误", e)
        return "101"
    print(resp)
    # 匹配头像地址
    pat_h = re.compile(
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    # 匹配名字
    pat_n = re.compile('-1,0,0,0,"(.*?)",0]}')
    try:
        headURL = re.findall(pat_h, resp)[0]
        name = re.findall(pat_n, resp)[0]
    except:
        return "1"
    return headURL


def download(headURL):
    global qqID
    resp = requests.get(headURL, headers=header).content
    md5 = getStrAsMD5(resp)
    # 空白头像 9e981dc7788599d9372c8381d776c554 6b3dc21f211fc653b3756c3392221293
    print(md5)
    if md5 == "9e981dc7788599d9372c8381d776c554":
        print(str(qqID) + " " + "空白头像")
        pass
    elif md5 == "6b3dc21f211fc653b3756c3392221293":
        print(str(qqID) + " " + "空白头像")
        pass
    elif md5 == "de1f6b4a58422bba344f94927dd90a9b":
        print(str(qqID) + " " + "空白头像")
        pass
    else:
        img = requests.get(headURL, headers=header).content
        name_b = validateTitle(name)
        with open("{0}\\img\\{1}.jpg".format(path, str(qqID) + " " + name_b), "wb") as f:
            f.write(img)
        with open("{0}\\qqList.txt".format(path), "a", encoding="utf-8") as l:
            l.write("qq号：" + str(qqID) + "  " + "网名：" + name + "\n")
        print(str(qqID) + " " + name, "已保存")


# qqID = "2734184475"
# url = getHead(qqID)
# download(url)
# qqList=["2734184475"]
# for qqID in range(1000000000, 9999999999):

def run():
    while True:
        try:
            qqID = random.randint(1000000000, 9999999999)
            url = getHead(qqID)
            if url == "1":
                print(qqID, "用户不存在")
                pass
            elif url == "101":
                print("用户不存在")
            else:
                download(url)
            print("-------------------------------")
        except Exception as p:
            print("大运行出现异常,停止2s", p)
            print("-------------------------------")
            time.sleep(2)


for i in range(5):
    run()
