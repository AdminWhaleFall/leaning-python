import smtplib
from email.mime.text import MIMEText

msg_from = "whalefall2020@163.com"  # 发送方
pwd = "BFEPKZGIINCMBEGM"  # 授权密码
to = "2734184475@qq.com"  # 接收方

subject = "这是Python发送的邮件"  # 主题
content = "<h1>你家着火了</h1>"  # 内容

msg = MIMEText(content, "html", "utf-8")  # msg邮件对象
msg["Subject"] = subject  # 主题
msg["From"] = msg_from
msg["To"] = to


try:
    ss = smtplib.SMTP_SSL('smtp.163.com', 994)  # smtp服务器地址
    ss.login(msg_from, pwd)
    ss.sendmail(msg_from, to, msg.as_string())
except Exception as e:
    raise e
else:
    print("不出意外的话应该是可以发送成功的叭")
