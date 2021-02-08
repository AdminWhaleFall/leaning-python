'''
Author: whalefall
Date: 2021-02-07 18:44:50
LastEditors: whalefall
LastEditTime: 2021-02-08 10:49:32
Description: ServerStatus|主文件
'''
import os
import sys
import time
from MailServer import *  # 导入邮箱模块
from order import *

# 循环检查网络
for i in range(1, 1001):
    
    network = checkNetwork()
    
    if network == "Success":

        print("[Suc]网络检查成功,开始检查邮箱模块")

        mailServer = checkMailServer()
        if mailServer == "Success":
            print("[Suc]邮箱模块正常! 开始启动监控!")
            break
        elif mailServer == "Error":
            print("[Error]邮箱模块异常")
            continue

    elif network == "Error":
        print("[Error]网络检查失败!检查第{}次".format(i))
    time.sleep(15)

#发送一封系统状态邮件












