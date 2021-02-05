'''
Author: whalefall
Date: 2021-02-04 18:08:27
LastEditors: whalefall
LastEditTime: 2021-02-04 20:33:02
Description: Q绑数据导入db
'''

import re
import sqlite3  # 数据库模块
import time

# 链接数据库
conn = sqlite3.connect(r"F:\Q绑数据\data.db")
c = conn.cursor()


def writeDB(qq, phone):
    try:
        res = c.execute(
            "INSERT INTO main.qq(qq,phone) VALUES(?,?)", (qq, phone))
        # print(qq,phone)
    except Exception as e:
        print("[1;30;41m[Error]提交数据库时出现错误!\033[0m")
    finally:
        pass
        # conn.commit()
        # conn.close()

    # writeDB("text","saas")


with open(r"F:\Q绑数据\新建文件夹\6.9更新总库2\6.9更新总库.txt", "r") as f:
    s_time = int(time.time())
    # 每次读取50MB数据不过分叭 60**2
    i = 0
    while True:
        try:
            # 一次读取多少字节(B) 1KB=2^10B 1MB=2^20 B 1GB=2^30B 1TG=2^40B
            data = f.readlines(50*2**20)
            i += 1
            # 判断是否获取完成
            if data == []:
                b_time = int(time.time())
                print("写入完成! 总耗时:{} s".format(b_time-s_time))
                break

            for result in data:
                # 正则匹配时可能发生错误
                result = result.replace("\n", "")
                pat = re.compile(r"(\d+)----(\d+)")
                qq = pat.findall(result)[0][0]
                phone = pat.findall(result)[0][1]
                # print(qq, phone)
                writeDB(qq, phone)

            # 批量插入之后再执行事务提交 这样会快很多很多!!!
            conn.commit()
            print("\033[1;30;44m[Suc]已读取到:{}MB (合:{}GB)\033[0m".format(
                i*50, round(i*50/1025, 3)))

        except Exception as e:
            print("\033[1;30;41m[Error]程序发生未知错误,但是一定不要让他停下来!\033[0m", e)
