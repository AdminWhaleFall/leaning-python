'''
Author: whalefall
Date: 2021-02-06 23:08:13
LastEditors: whalefall
LastEditTime: 2021-02-06 23:19:24
Description: 服务器监控中的发送邮件模块
'''
import zmail
# 邮箱配置:
# 邮箱密码/授权码
sendEmail = "whalefall2020@163.com"
password = "BFEPKZGIINCMBEGM"

# smtp发信配置
smtp_host = "smtp.163.com"
smtp_port = 994
smtp_ssl = True  # 是否使用ssl加密传输发信

# pop收信配置
pop_host = "pop.163.com"
pop_port = 995

# 自定义 邮件服务器对象
server = zmail.server(
    username=sendEmail,
    password=password,
    smtp_host=smtp_host,
    smtp_port=smtp_port,
    smtp_ssl=smtp_ssl,
    pop_host=pop_host,
    pop_port=pop_port,
    timeout=60,
    debug=False,
    log=None
)

# print(server.smtp_able(), server.pop_able())
if server.smtp_able() and server.pop_able():
    print("[Suc]邮箱模块运行正常!")
else:
    print("[Error]邮箱模块运行异常 smtp:{} pop:{}".format(server.smtp_able(),server.pop_able()))
