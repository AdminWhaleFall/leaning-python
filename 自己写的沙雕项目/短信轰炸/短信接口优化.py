'''
Author: whalefall
Date: 2021-01-23 10:52:05
LastEditors: whalefall
LastEditTime: 2021-01-23 10:53:59
Description: 基于python的短信轰炸接口检验+排除脚本,需要结合PHP程序使用。
'''

import json
import random
import re
import sys
import time

import pymysql
import requests
from fake_useragent import UserAgent

# 获取秒级时间戳
t = str(int(time.time()))
# print(t)

# 获取脚本路径
path = sys.path[0]

# 数据库参数
host = "192.168.101.4"
user = "root"
passwd = "123456"


def getApiData():
    try:
        # 打开数据库连接
        conn = pymysql.connect(host, user=user, passwd=passwd, port=3306)
        # 获取游标
        cursor = conn.cursor()
        # print(cursor)
    except Exception as u:
        print("数据库连接失败!", u)

    sql = "SELECT id,url,post,status FROM api.msg_api;"
    r = cursor.execute(sql)

    # 获取数据
    # fetchall遍历execute执行的结果集。取execute执行后放在缓冲区的数据，遍历结果，返回数据。
    # 返回的数据类型是元组类型，每个条数据元素为元组类型:(('第一条数据的字段1的值','第一条数据的字段2的值',...,'第一条数据的字段N的值'),(第二条数据),...,(第N条数据))
    data = cursor.fetchall()
    # print(data[1][1])

    # 关闭游标和数据库连接
    cursor.close()
    conn.close()

    ListData = []
    # 循环获取元组的数据 将元组转换为json
    for r in data:
        # List为一个字典
        List = {}
        # print(r)
        List["id"] = str(r[0])
        List["url"] = str(r[1])
        List["post"] = str(r[2])
        # print(List)

        # 在列表中添加字典
        ListData.append(List)

    # print(ListData)

    # 使用json.dumps将数据转换为json格式，json.dumps方法默认会输出成这种格式"\u5377\u76ae\u6298\u6263"，加ensure_ascii=False，则能够防止中文乱码。
    # JSON采用完全独立于语言的文本格式，事实上大部分现代计算机语言都以某种形式支持它们。这使得一种数据格式在同样基于这些结构的编程语言之间交换成为可能。
    # json.dumps()是将原始数据转为json（其中单引号会变为双引号），而json.loads()是将json转为原始数据。
    # jsondata = json.dumps(ListData, ensure_ascii=False)
    # print(jsondata)

    return ListData

    # with open(r"{}//短信接口.json".format(path),"a") as f:
    #     f.write(jsondata)


# 字符串关键词替换
def tihuan(url, phone):
    # 获取时间戳
    t = str(int(time.time()))
    # 关于string的replace方法，需要注意replace不会改变原string的内容。
    a = url.replace("[手机号码]", str(phone))
    b = a.replace("[时间]", t)
    # print(b)
    return b


# 请求Post接口函数
def respApiPost(id, url, post):
    print("----------------------------------")
    print("ID:{} 的Post请求结果:".format(id), "请求地址:", url, "post内容:", post)
    try:
        # 代理ip请求方法 暂时咕咕着
        # resp = requests.post(url, json=post, headers={"User-Agent": str(UserAgent().random)}, timeout=8,
        #                      proxies={"http": "http://{}".format(httpProxy), "https": "https://{}".format(httpsProxy)})

        resp = requests.post(url, data=post, headers={"User-Agent": str(UserAgent().random)})
        result = resp.text
    except Exception as e:
        # print("ID:{} 请求错误".format(id), e)
        result = "0"

    print(result)

    return result


# 请求Get接口函数
def respApiGet(id, url):
    print("----------------------------------")
    print("ID:{} 的Get请求结果:".format(id), "请求地址:", url)
    try:
        # 代理ip请求方法 暂时咕咕着
        # resp = requests.post(url, headers={"User-Agent": str(UserAgent().random)}, timeout=8,
        #                      proxies={"http": "http://{}".format(httpProxy), "https": "https://{}".format(httpsProxy)},
        #                      )

        resp = requests.post(url, headers={"User-Agent": str(UserAgent().random)})
        result = resp.text
    except Exception as e:
        print("ID:{} 请求错误".format(id), e)
        result = "0"

    print(result)

    return result


# 停用/启用 短信接口函数
def upnApi(status, id):
    # 连接数据库
    try:
        # 打开数据库连接
        conn = pymysql.connect(host, user=user, passwd=passwd, port=3306)
        # 获取游标
        cursor = conn.cursor()
        # print(cursor)
    except Exception as u:
        print("数据库连接失败!", u)

    # 停用为0 启用为1
    sql = "update api.msg_api set status = %s where id = %s;"
    cursor.execute(sql, (str(status), str(id)))
    # 一定要提交更改
    cursor.connection.commit()

    if status == "0":
        print("ID:{} 已停用".format(id))
    elif status == "1":
        print("ID:{} 已启用".format(id))
    else:
        print("ID:{} 输入的status参数有误".format(id))

    # 关闭游标和数据库连接
    cursor.close()
    conn.close()


httpProxy = "61.160.210.234:808"
httpsProxy = "61.160.210.234:808"


# 运行函数
def run():
    data = getApiData()
    phone = "15017662289"
    for f in data:
        id = f["id"]
        url = tihuan(f["url"], phone)

        if f["post"] == "":
            GetReturn = respApiGet(id, url)

            # 请求失败自动停用
            if GetReturn == "0":
                upnApi("0", id)
                # 自动停用后不再进入手动停用
                continue

            # 人工判断手动停用

            # while True:
            #     setIDstatus = input("是否停用ID:{}接口(停用:0/不停用:1)".format(id))
            #     if setIDstatus == "0":
            #         upnApi("0", id)
            #         break
            #     elif setIDstatus == "1":
            #         upnApi("1", id)
            #         break
            #     else:
            #         print("输入的参数有误 请重新输入")


        else:
            post = tihuan(f["post"], phone)
            PostReturn = respApiPost(id, url, post)

            # 请求失败自动停用
            if PostReturn == "0":
                upnApi("0", id)
                # 自动停用后不再进入手动停用
                continue

            # 人工判断手动停用
            # while True:
            #     setIDstatus = input("是否停用ID:{}接口(停用:0/不停用:1)".format(id))
            #     if setIDstatus == "0":
            #         upnApi("0", id)
            #         break
            #     elif setIDstatus == "1":
            #         upnApi("1", id)
            #         break
            #     else:
            #         print("输入的参数有误 请重新输入")

        # time.sleep(1)


run()
