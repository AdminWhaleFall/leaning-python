import base64 #base64模块
import requests
import random
import time
from fake_useragent import UserAgent

def randomEmail():
	#随机生成邮箱前缀
	email_start=str(random.randint(1000000000,9000000000))
	#随机生成邮箱后缀
	email_end=["qq.com","163.com","gmail.com","126.com","sian.com","soho.com","yeah.com","139.com"]
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


#构造请求头
header={
	"Content-Type":"application/x-www-form-urlencoded",
	"User-Agent":"Dalvik/2.1.0 (Linux; U; Android 6.0; HUAWEI GRA-TL00 Build/HUAWEIGRA-TL00)",
	"Host":"service-20f3c4xu-1254093318.gz.apigw.tencentcs.com",
	"Connection":"Keep-Alive",
	"Accept-Encoding":"gzip",
	"Content-Length":"58",
}


#注册url
url="https://service-20f3c4xu-1254093318.gz.apigw.tencentcs.com/release/reg"

def reg():
	randomEmail()
	randomPwd()
	print("生成账号:",email,"生成密码:",pwd)
	str2b64()
	#构造请求体
	datafrom={
		"email":email,
		"password":pwd,
	}
	resp=requests.post(url,data=datafrom,headers=header)
	return resp

t=0
while True:
	resp=reg()
	# print("服务器状态码:",resp.status_code)
	rep=resp.json()
	# print(rep)
	if rep==107:
		print("注册账号太多可能被服务器拒绝了叭")
	else:
		try:
			t=t+1
			print("脚本已注册:",t)
			print("服务器响应注册时间:",rep['createdAt'])
			print("响应注册邮箱:",rep['email'])
			print("响应注册总人数:",rep['username'])
		except Exception as o:
			t=t-1
			print("服务器响应未知错误:",rep)
		
	print("----------------------")
	time.sleep(1)

if __name__ == '__main__':
	run()


