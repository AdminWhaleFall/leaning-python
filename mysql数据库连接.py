# coding=utf-8
import pymysql
import requests
import re
import hashlib
import sys
import random
import time

host = "134.175.56.69"
user = "root"
passwd = "123456"

try:
    # 打开数据库连接
    conn = pymysql.connect(host, user=user, passwd=passwd, port=3306,database="QQList")
    # 获取游标
    cursor = conn.cursor()
    # print(cursor)
except Exception as u:
    print("数据库连接失败!", u)


# 执行sql语句execute和executemany
# execute:执行单条的sql语句，执行成功后返回受影响的行数
# 参数说明：
# query：要执行的sql语句，字符串类型
# args：可选的序列或映射，用于query的参数值。如果args为序列，query中必须使用%s做占位符；如果args为映射，query中必须使用%(key)s做占位符

# executemany:批量执行sql语句，比如批量插入数据，执行成功后返回受影响的行数
# query：要执行的sql语句，字符串类型
# args：嵌套的序列或映射，用于query的参数值

# 创建pythonBD数据库 执行成功后返回受影响的行数
# 创建一个QQ数据库
# cursor.execute('CREATE DATABASE IF NOT EXISTS QQList DEFAULT CHARSET utf8 COLLATE utf8_general_ci;')
#
# 创建user表
# cursor.execute('CREATE TABLE user;')

# 创建user表
# sql = "CREATE TABLE user (name VARCHAR(255), id VARCHAR(255))"
# try:
#     cursor.execute(sql)
# except Exception as y:
#     print(y)

# # 先关闭游标
# cursor.close()
# # 再关闭数据库连接
# conn.close()

# print('创建QQ数据库成功', r)

def writeMysql(qq_name, id1):
    sql1 = "INSERT INTO `user` (`name`, `id`) VALUES (%s, %s)"
    cursor.execute(sql1, (qq_name, id1))
    # 一定要提交更改
    cursor.connection.commit()
    # print(r)


writeMysql("我爱你","sas")

# cursor.close()
# conn.close()

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


# 获取QQ昵称
def getHead(qqID):
    global name
    url = "https://r.qzone.qq.com/fcg-bin/cgi_get_portrait.fcg?uins=" + str(qqID)
    try:
        resp = requests.get(url, headers=header).content.decode(encoding="gbk")
    except Exception as e:
        print("可能是编码错误", e)
        return "101"
    # print(resp)
    # 匹配头像地址
    pat_h = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    # 匹配名字
    pat_n = re.compile('-1,0,0,0,"(.*?)",0]}')
    try:
        headURL = re.findall(pat_h, resp)[0]
        name = re.findall(pat_n, resp)[0]
    except:
        return "1"
    return headURL


# 通过头像检验是否为活跃QQ号
def download(headURL):
    resp = requests.get(headURL, headers=header).content
    md5 = getStrAsMD5(resp)
    # 空白头像 9e981dc7788599d9372c8381d776c554 6b3dc21f211fc653b3756c3392221293
    # print(md5)
    if md5 == "9e981dc7788599d9372c8381d776c554":
        # print(str(qqID) + " " + "空白头像")
        return "0"
    elif md5 == "6b3dc21f211fc653b3756c3392221293":
        # print(str(qqID) + " " + "空白头像")
        return "0"
    elif md5 == "de1f6b4a58422bba344f94927dd90a9b":
        # print(str(qqID) + " " + "空白头像")
        return "0"
    else:
        return qqID

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
            qqID = download(url)
            if qqID == "0":
                # print(qqID, name, "空白头像")
                pass
            else:
                print(qqID, name)
                writeMysql(qqID,name)
                print("-------------------------------")
    except Exception as p:
        print("大运行出现异常,停止2s", p)
        print("-------------------------------")
        time.sleep(2)
