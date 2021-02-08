'''
Author: whalefall
Date: 2021-02-06 23:08:13
LastEditors: whalefall
LastEditTime: 2021-02-08 10:41:35
Description: ServerStatus|邮件模块
感谢:https://github.com/zhangyunhao116/zmail/blob/master/README-cn.md
'''
import zmail
import sys
import os

py_path = sys.path[0]

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

# 管理员邮箱
adminEmail="whalefall9420@qq.com"


# 发送邮件文字内容
def sendTxtEmail(tomail, content):
    # 构造邮箱
    mail = {
        'subject': 'GoodbyPi|邮件通知',
        'content_text': content,
        # 'content_html':"", # 支持HTML
        # 'attachments':"" # 附件 可为 字符串 或者 一个由字符串组成的列表
    }

    # 发送邮件 接收者可以是一个列表 cc:使用抄送 可以是一个列表,使用元组为其命名
    server.send_mail(tomail, mail, cc=[("admin", "tgc@sky.163.com")])


# 判断邮箱服务可用性 ->true:发送邮件给主控  ->false:抛出错误
def checkMailServer():
    try:
        global server
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

        if server.smtp_able() and server.pop_able():
            print("[Suc]邮箱模块运行正常!")
            sendTxtEmail(adminEmail, "ServerStatus|已启动监控服务,邮箱模块运行正常 ヽ(✿ﾟ▽ﾟ)ノ")
            return "Success"
        else:
            print("[Error]邮箱模块运行异常 smtp:{} pop:{}".format(
                server.smtp_able(), server.pop_able()))
            return "Error"
    except Exception as e:
        print("[Error]邮箱模块出现未知错误!请检查各参数 {}".format(e))

# checkMailServer()


# 获取最新邮件
# getMail=server.get_latest()
# print(server.stat())

# 获取指定邮件 多个邮件的话返回一个列表
# maiList = server.get_mails(subject='GoodbyPi')
# for mail in maiList:
#     zmail.show(mail)
#     # 将邮件的附件存储到target_path。如果不指定，target_path将会是当前目录。如果overwrite为True，写入过程将会覆盖可能存在的同名文件
#     zmail.save_attachment(mail, overwrite=True,target_path="{}//download".format(py_path))
