# zmail 邮件发送模块
# GitHub地址：https://github.com/ZYunH/zmail/blob/master/README-cn.md
import zmail
import datetime
#邮箱密码/授权码
sendEmail="whalefall2020@163.com"
password="BFEPKZGIINCMBEGM"
#smtp发信配置
smtp_host="smtp.163.com"
smtp_port=994
smtp_ssl=True #是否使用ssl加密传输发信
#pop收信配置
pop_host="pop.163.com"
pop_port=995
# 自定义 邮件服务器对象 
ServerPop=zmail.server(sendEmail,password,pop_host=pop_host,pop_port=pop_port)
ServerStmp=zmail.server(sendEmail,password,smtp_host=smtp_host,smtp_port=smtp_port,smtp_ssl=smtp_ssl)
#获取最新一封邮件
# serverPop.get_latest()

# 获取指定ID的邮件 同样将邮件设置为已读
ServerPop.get_mail(1)

# 解析邮件
# print(mail['subject']) #取出邮件主题
# zmail.show(mail) #打印邮件

#查看邮件的所有内容
# for k,v in mail.items():
# 	print(k,v)

# 获取邮箱状态 返回元组 (邮件未读数量, 邮件大小)
print(ServerPop.stat())

# 获取指定ID的邮件（位于1至邮件数量） 同样将邮件设置为已读
# zmail.show(serverPop.get_mail(2))

#取出指定范围内的邮件
mails=ServerPop.get_mails(subject=None,start_time=None,end_time=None,sender=None,start_index=1,end_index=1)
# zmail.show(mails)
print(mails[0]["subject"]) #取出主题
print(mails[0]['from'])

#删除指定ID的邮件
# serverPop.delete(2)

#stmp pop 运行状态
print(ServerPop.smtp_able())
print(ServerStmp.pop_able())

#发送email
#构造email
def sendEmail(tomail):
	now = datetime.datetime.now()
	time=now.strftime("%Y-%m-%d %H:%M:%S")
	html='''
	<html>
	 <head></head>
	 <body>
	  <table style="width:99.8%;height:99.8%"> 
	   <tbody> 
	    <tr> 
	     <td style="background:#fafafa url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAICAYAAADED76LAAAAy0lEQVQY0x2PsQtAYBDFP1keKZfBKIqNycCERUkMKLuSgZnRarIpJX8s3zfcDe9+794du+8bRVHQOI4wDAOmaULTNDDGYFkWMVVVQUTQdZ3iOMZxHCjLElVV0TRNYHVdC7ptW6RpSn3f4wdJkiTs+w6WJAl4DcOAbdugKAq974umaRAEARgXn+cRW3zfFxuiKCJZloXGHMeBbdv4Beq6Duu6Issy7iYB8Jbnucg8zxPLsggnj/zvIxaGIXmeB9d1wSE+nOeZf4HruvABUtou5ypjMF4AAAAASUVORK5CYII=)"> 
	      <div style="border-radius:10px;font-size:13px;color:#555;width:666px;font-family:'Century Gothic','Trebuchet MS','Hiragino Sans GB','微软雅黑','Microsoft Yahei',Tahoma,Helvetica,Arial,SimSun,sans-serif;margin:50px auto;border:1px solid #eee;max-width:100%;background:#fff repeating-linear-gradient(-45deg,#fff,#fff 1.125rem,transparent 1.125rem,transparent 2.25rem);box-shadow:0 1px 5px rgba(0,0,0,.15)"> 
	       <div style="width:100%;background:#49BDAD;color:#fff;border-radius:10px 10px 0 0;background-image:-moz-linear-gradient(0deg,#43c6b8,#ffd1f4);background-image:-webkit-linear-gradient(0deg,#43c6b8,#ffd1f4);height:66px">
	        <h1 style="font-size:25px;word-break:break-all;padding:23px 32px;margin:0;background-color:hsla(0,0%,100%,.4);border-radius:10px 10px 0 0;color:red">{0} 鲸云服务器运行状态</h1>
	       </div> 
	       <div style="margin:40px auto;width:90%"> 
	        <!-- <p>Whale Fall鲸落，您曾在文章《<a href="https://www.mk857.cn/apply.html" style="text-decoration:none;color:#12addb" target="_blank">申请友链</a>》上发表评论:</p>  -->
	        <!-- <p style="background:#fafafa repeating-linear-gradient(-45deg,#fff,#fff 1.125rem,transparent 1.125rem,transparent 2.25rem);box-shadow:0 2px 5px rgba(0,0,0,.15);margin:20px 0;padding:15px;border-radius:5px;font-size:14px;color:#555">&gt;网站名称：鲸落の小窝 &gt;地址：https://whalefall.online/ &gt;头像地址：http://q1.qlogo.cn/g?b=qq&amp;nk=2734184475&amp;s=640 ![头像](http://q1.qlogo.cn/g?b=qq&amp;nk=2734184475&amp;s=640) &gt;简介：一鲸落，万物生</p>  -->
	        <p>梦轲 给您的回复如下：</p> 
	        <p style="background:#fafafa repeating-linear-gradient(-45deg,#fff,#fff 1.125rem,transparent 1.125rem,transparent 2.25rem);box-shadow:0 2px 5px rgba(0,0,0,.15);margin:20px 0;padding:15px;border-radius:5px;font-size:14px;color:#555">友链已添加</p>
	        <p>您可以<a href="http://www.baidu.com/" style="text-decoration:none;color:#12addb" target="_blank">登录面板查看实时状态</a>，欢迎再次光临 <a href="https://www.mk857.cn/" style="text-decoration:none;color:#12addb" target="_blank">鲸云|服务器</a>。</p> 
	        <p>请注意：此邮件由 <a href="https://www.mk857.cn/" style="color:#12addb" target="_blank">鲸云|服务器</a> 自动发送，请勿直接回复。</p> 
	        <p>若此邮件不是您请求的，请忽略并删除！</p> 
	       </div> 
	      </div> </td> 
	    </tr> 
	   </tbody> 
	  </table>
	 </body>
	</html>
	'''.format(time)
	mail={
		"subject":"鲸云|邮件通知",
		#可自定义发送者的名字
		# "from":"鲸落云 <whalefall@whalefall.online>",
		"content_text":"鲸云|Python邮件通知测试",
		#可读取HTML文件
		"content_html":html,
		#附件
		"attachments":r"C:\Users\27341\Desktop\name.txt",

	}

	#发件人可以给一整个列表
	ServerStmp.send_mail(tomail,mail)


sendEmail("2734184475@qq.com")


