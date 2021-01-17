import requests
from lxml import etree
import re
from time import *
#邮件发送模块
import smtplib
from email.mime.text import MIMEText

#轰炸请求接口 需PHP搭建
url="http://192.168.101.4:81/api.php?"
key="goodby"
# phone="15017662284"
header={
		"User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; EVA-AL10 Build/HUAWEIEVA-AL10;\
		 wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89\
		  Mobile Safari/537.36 T7/11.20 SP-engine/2.16.0 baiduboxapp/11.20.0.14 (Baidu; P1 8.0.0)",
	}
#请求轰炸
def SendHz(key,phone):
	#get请求内容
	data_send={
	"act":"user",
	"key":key,
	"phone":phone,
	}

	try:
		#发送hz请求 par|ams 参数
		resp_hz=requests.get(url,params=data_send).json()
		msg=resp_hz['msg']
	

		if msg=='':
			SendHzStatus="鲸云请求发送成功啦!\n被hz的小可怜:"+phone
		else:
			SendHzStatus="key错误:"+msg

	except Exception as e:
		#如果服务器死机或者请求发不出去,json化时失败
		SendStatus="卑微的服务端响应异常:"+e

	return SendHzStatus

#查询轰炸
def SendLog(key):
	#查询get内容
	data_log={
	"act":"log",
	"key":key,
	}

	try:
		#发送查询log请求
		resp_log=requests.get(url,params=data_log).json()
		
		if resp_log['msg']=="查询成功":
			#解析查询数据
			log=resp_log['data'] #返回列表
			# 遍历列表
			# 设置循环次数限制，防止轰炸过多,超出信息长度限制
			i=0
			logMsg=""
			for l in log:
				#i循环次数
				i=i+1
				if i>1000: #最大输出日志数
					break
				phone=l['phone'] #手机号码
				# print(phone)
				where=phoneWhere(phone)
				date=l['date'] #轰炸时间
				print("手机号:"+phone+"("+where+")"+" hz时间:"+date+"\n")
				logMsg="手机号:"+phone+"("+where+")"+" hz时间:"+date+"\n"+logMsg
				# logMsg="手机号:"+phone+" hz时间:"+date+"\n"+logMsg

		else:
			logMsg="查询有误,"+resp_log['msg']
			
	except Exception as e:
			logMsg="服务器错误"

	logMsg="查询结果: 轰炸总次数:"+str(len(log))+"\n"+logMsg

	return logMsg

#手机号归属地查询来源api:百度免费api
def phoneWhere(phone):

	api="https://api.asilu.com/phone/"
	
	datafrom={
		"phone":phone,
	}
	
	try:
		#好像无限制 速度还行
		resp=requests.get(url=api,headers=header,params=datafrom).json()
		where=resp["province"]+resp["city"]+resp["sp"]
	except Exception as e:
		print("请求api失败 切换api",e)

		try:
			b1_time=time()
			# ip.cn爬虫 死都能使用
			api="http://ip.cn/db?num="+str(phone)
			resp=requests.get(url=api,headers=header).content.decode()
			#用正则查找所在城市和运营商
			pat=re.compile(r"城市: (.*?)<br />")
			where=re.findall(pat,resp)
			where=where[0]
		except Exception as e:
			where="未知"
		finally:
			e1_time=time()	

		print("耗时:",str(round(e1_time-b1_time,2))+"s")

	# try:
	# 	b_time=time()
	# 	# ip.cn爬虫
	# 	api="http://ip.cn/db?num="+str(phone)
	# 	resp=requests.get(url=api,headers=header).content.decode()
	# 	#用正则查找所在城市和运营商
	# 	pat=re.compile(r"城市: (.*?)<br />")
	# 	where=re.findall(pat,resp)
	# 	where=where[0]
	# 	e_time=time()
	# 	print("耗时:",e_time-b_time)
	# except Exception as e:
	# 	where="未知"
				
	return where

#邮箱发送
def sendmail(content,sendId):
	msg_from="whalefall2020@163.com" #发送方
	pwd="BFEPKZGIINCMBEGM" #授权密码
	to=sendId #接收方

	subject="鲸云|顾白云轰炸日志" #主题
	#文本 支持HTML 需修改构造邮件参数
	content=content

	#构造邮件 支持HTML 传入以下参数
	msg=MIMEText(content,"html","utf-8") #msg邮件对象
	#邮件中的构造跟字典类似,把subject赋值给msg字典中的Subject键
	msg["Subject"]=subject #主题
	msg["From"]=msg_from
	msg["To"]=to

	try:
		ss=smtplib.SMTP_SSL('smtp.163.com',994) #smtp服务器地址
		ss.login(msg_from,pwd)
		ss.sendmail(msg_from,to,msg.as_string())
	except Exception as e:
		raise e
	else:
		print("不出意外的话应该是可以发送成功的叭")



'''
#发送轰炸 返回发送状态
SendHz(key,phone) 
#查询轰炸 返回查询结果
SendLog(key)
'''
begin_time = time()

log=SendLog(key)
print(log)
# where=phoneWhere(16616929029)
# print(where)

sendmail(log,"2734184475@qq.com")
sleep(10)
sendmail(log,"hellowert@qq.com")

end_time = time()
print("程序总运行时长:",str(round(end_time-begin_time,2))+"s")





