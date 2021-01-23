'''
Author: whalefall
Date: 2021-01-23 10:59:09
LastEditors: whalefall
LastEditTime: 2021-01-23 11:03:31
Description: 针对于doing专注软件的批量注册程序,源作者[干物檬]设置了IP限制注册,所以该项目也包含了获取[免费可用代理ip]的函数
Tis:目前[肝物檬]添加了邮箱限制注册,处于人道主义精神我就不再搞他了。
'''


import base64  # base64模块
import random
import threading
import time

import requests
from fake_useragent import UserAgent

from http_Proxy import get_proxy


def randomEmail():
	#随机生成邮箱前缀
	email_start=str(random.randint(1000000000,9000000000))
	#随机生成邮箱后缀
	email_end=["qq.com","163.com","gmail.com","126.com","139.com"]
	email_end=random.choice(email_end)
	global email
	email=email_start+"@"+email_end

#生成随机密码
def randomPwd():
	global pwd
	for i in range(8):
		pwd = 'abcdefghijklmnopqrstuvwxyz1234567890'
		# 号内的迭代对象（如列表）使用s字符串作为链接将迭代对象中的元素拼接成一个字符串，返回该字符串。
		pwd = random.sample(pwd,8)
	pwd=''.join(pwd)

def str2b64():
	#在子程序中对全局变量的操作,要声明全局变量
	global email
	# 需要转成2进制格式才可以转换
	email=email.encode()
	email=base64.b64encode(email).decode()

	global pwd
	# 需要转成2进制格式才可以转换
	pwd=pwd.encode()
	pwd=base64.b64encode(pwd).decode()

#注册url
url="http://121.199.37.166/app/v1/reg.php"

def reg(ip):
	header={"UserAgent":str(UserAgent().random)}
	randomEmail()
	randomPwd()
	print("生成账号:",email,"生成密码:",pwd)
	str2b64()
	#构造请求体
	datafrom={
		"email":email,
		"password":pwd,
	}
	#代理请求
	proxy={
		"http":"http://"+ip
	}
	try:
		resp = requests.post(url, data=datafrom, headers=header, proxies=proxy).text
	except Exception as e:
		resp="请求失败"+str(e)

	return resp

# t=0
# while True:
# 	resp=reg()
# 	# print("服务器状态码:",resp.status_code)
# 	rep=resp.json()
# 	# print(rep)
# 	if rep==107:
# 		print("注册账号太多可能被服务器拒绝了叭")
# 	else:
# 		try:
# 			t=t+1
# 			print("脚本已注册:",t)
# 			print("服务器响应注册时间:",rep['createdAt'])
# 			print("响应注册邮箱:",rep['email'])
# 			print("响应注册总人数:",rep['username'])
# 		except Exception as o:
# 			t=t-1
# 			print("服务器响应未知错误:",rep)
#
# 	print("----------------------")
# 	time.sleep(1)

ipList = get_proxy("http",10)
# ipList=['27.208.27.186:8060', '203.99.133.29:80', '119.28.233.135:8080', '205.185.115.100:8080', '51.159.93.12:5836', '117.84.155.112:8118', '219.85.138.43:80', '105.27.238.163:80', '8.208.88.202:80', '203.202.245.58:80', '218.66.253.144:8800', '103.122.98.13:8080', '101.4.136.34:81', '80.241.222.138:80', '105.27.238.167:80', '47.115.63.52:8888', '1.2.183.55:8080', '105.27.237.28:80', '218.66.253.146:8800', '118.25.13.185:3128', '51.77.229.110:3128', '105.27.237.27:80', '196.52.65.100:80', '105.27.238.161:80', '122.234.168.96:8060', '196.52.80.140:80', '183.88.46.230:8080', '196.52.58.53:80', '58.220.95.34:10174', '118.27.18.60:8081', '191.235.96.205:80', '176.9.63.62:3128', '82.124.211.87:3128', '196.52.80.72:80', '139.99.88.26:8080', '178.33.251.230:3129', '139.99.102.114:80', '116.197.129.243:37822', '5.252.192.100:5836', '105.27.237.30:80', '221.180.170.104:8080', '105.27.238.160:80', '165.22.36.75:8888', '51.79.165.33:8080', '211.137.52.159:8080', '8.210.194.45:80', '14.207.129.148:8080', '58.147.170.114:8085', '182.48.79.85:8080', '5.252.192.98:5836', '173.82.17.188:5836']

def run(name):
	while True:
		ip=random.choice(ipList)
		resp=reg(ip)
		print("线程"+name,resp)

t1=threading.Thread(target=run,args=("1",))
t2=threading.Thread(target=run,args=("2",))
t3=threading.Thread(target=run,args=("3",))
t4=threading.Thread(target=run,args=("4",))
t5=threading.Thread(target=run,args=("5",))
t6=threading.Thread(target=run,args=("6",))
t7=threading.Thread(target=run,args=("7",))
t8=threading.Thread(target=run,args=("8",))
t9=threading.Thread(target=run,args=("9",))
t10=threading.Thread(target=run,args=("10",))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()

