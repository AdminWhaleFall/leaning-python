# 邮件发送方(发送方地址,发送方客户端授权密码,SMTP服务器地址)
# 内容
# 邮件接收方
import smtplib
from email.mime.text import MIMEText

msg_from="whalefall2020@163.com" #发送方
pwd="BFEPKZGIINCMBEGM" #授权密码
to="2734184475@qq.com" #接收方

subject="这是Python发送的邮件" #主题
#文本 支持HTML 需修改构造邮件参数
content="<h1>你家着火了</h1>"

#构造邮件 支持HTML 传入以下参数
msg=MIMEText(content,"html","utf-8") #msg邮件对象
#邮件中的构造跟字典类似,把subject赋值给msg字典中的Subject键
msg["Subject"]=subject #主题
msg["From"]=msg_from
msg["To"]=to

# #发送邮件
# #以SMTP ssl安全加密协议发送邮件
# ss=smtplib.SMTP_SSL("",端口) #smtp服务器地址
# ss.login(msg_from,pwd) #登录 账号,密码
# # 发送邮件 发送方 接收方 内容(灵活转码)
# ss.sendmail(msg_from,to,msg.as_string())

# 对异常的处理
try:
	#发送邮件
	#以SMTP ssl安全加密协议发送邮件
	ss=smtplib.SMTP_SSL('smtp.163.com',994) #smtp服务器地址
	ss.login(msg_from,pwd) #登录 账号,密码
	# 发送邮件 发送方 接收方 内容(灵活转码)
	ss.sendmail(msg_from,to,msg.as_string())
except Exception as e:
	raise e
else:
	print("不出意外的话应该是可以发送成功的叭")


