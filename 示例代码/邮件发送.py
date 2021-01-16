import smtplib
from email.mime.text import MIMEText

msg_from="te***126.com" #发送方
pwd="123***1a"#授权码
to="2***616@qq.com"

subject="这是python发送的邮件！"
content="<h1>你家着火了！</h1>"

#构造邮件
msg=MIMEText(content,"html","utf-8") #msg邮件对象
msg["Subject"]=subject
msg["From"]=msg_from
msg["To"]=to

#发送邮件
try:
	ss=smtplib.SMTP_SSL("smtp.126.com",465)
	ss.login(msg_from,pwd)
	ss.sendmail(msg_from,to,msg.as_string()) #发送
	print("发送成功！")
except Exception as e:
	print("发送失败！详情：",e)
