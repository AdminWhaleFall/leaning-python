'''
Author: whalefall
Date: 2021-02-04 18:08:27
LastEditors: whalefall
LastEditTime: 2021-02-07 10:15:25
Description: Q绑数据导入sqlite和MySQL
'''

import re
import sqlite3  # sqlite数据库模块
import time

import pymysql  # mysql数据模块


# 写入sqlite数据库,因为本地文件不存在链接中断的情况,所以一开始就链接数据库,不用再函数里面连接
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


# mysql数据库参数:
host = "203.195.135.71"
user = "root"
passwd = "123456"
# 初始化mysql数据库


def startMysql():
    try:
        # 打开数据库连接
        conn = pymysql.connect(host, user=user, passwd=passwd, port=3306)
        # 获取游标
        cursor = conn.cursor()

        # 新建数据库 如果没有就新建 无就没反应
        sqlNewDatabases = '''
        CREATE DATABASE
        if NOT EXISTS {0}
        DEFAULT charset utf8 COLLATE utf8_general_ci;
        '''.format("qq")

        # 新建数据表 设置QQ为主键,[以防有重复但是不会继续进行下去,导致数据写少了]
        sqlNewTable = '''
        CREATE TABLE if not exists {0}.{0} ( 
            `qq` varchar(255), 
            `phone` varchar(255),
            primary key (`qq`)
            );
        '''.format("qq")

        cursor.execute(sqlNewDatabases)
        cursor.execute(sqlNewTable)

        # 写感谢信息[狗头]
        cursor.execute('''
            CREATE TABLE if not exists {0}.thank ( 
            `author` varchar(255),
            `content` varchar(255)
            );
            '''.format("qq"))
        cursor.execute('''
        insert into {0}.thank (`author`,`content`) values
        ("光之子","谢谢您提供的MySQL数据库,新年快乐！");
        '''.format("qq")
        )

        # 一定要提交更改
        cursor.connection.commit()

    except pymysql.err.ProgrammingError as e:
        print("[Error]MySql语法错误,请检查sql语句!")
        raise e
    except Exception as e:
        print("[Error]执行初始化MySql数据库失败!", e)
        raise e
    else:
        print("[Suc]MySql数据库初始化成功!")
        return "0"


# 写入mysql数据库
# set global max_allowed_packet = 1024*1024*1024 修改大小限制
def writeMysql(aegs):
    
    # 插入时用  INSERT IGNORE INTO 表名 VALUES (......),可以避免出现重复，插入也不会终止 参考
    # 指令	已存在	不存在	
    # insert	报错	插入	
    # insert ignore	忽略	
    # replace	替换	插入
    
    # https://blog.csdn.net/mouday/article/details/81281946
    sql = '''
    insert IGNORE into qq.qq (qq,phone) values (%s,%s)
    '''
    try:
        # 打开数据库连接
        conn = pymysql.connect(host, user=user, passwd=passwd, port=3306)
        # 获取游标
        cursor = conn.cursor()
        cursor.executemany(sql, aegs)

    except Exception as e:
        print("[Error]写入数据库时出现异常", e)

    finally:
        cursor.close()
        conn.commit()
        conn.close()


# 初始化
resMysql = startMysql()
if resMysql != "0":
    print("MySQL初始化异常!")


# 运行部分
with open(r"F:\Q绑数据\6.9更新总库.txt", "r") as f:
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

            aegs = []
            for result in data:
                # 正则匹配时可能发生错误
                result = result.replace("\n", "")
                pat = re.compile(r"(\d+)----(\d+)")
                try:
                    qq = pat.findall(result)[0][0]
                    phone = pat.findall(result)[0][1]
                except Exception:
                    print("\033[1;30;41m[Error]有一条格式有误,无法录入,但不影响后面的数据!\033[0m")
                else:
                    # print(qq, phone)
                    # writeDB(qq, phone)
                    # 新建元组
                    tup = (qq, phone)
                    aegs.append(tup)

            writeMysql(aegs)

            # sqlite批量插入之后再执行事务提交 这样会快很多很多!!!
            # conn.commit()

            print("\033[1;30;44m[Suc]已读取到:{}MB (合:{}GB)\033[0m".format(
                i*50, round(i*50/1025, 3)))

        # 改后应该不会出现这种情况了
        except Exception as e:
            print("\033[1;30;41m[Error]程序发生未知错误,但是一定不要让他停下来!\033[0m", e)

