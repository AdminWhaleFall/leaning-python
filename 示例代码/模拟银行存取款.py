import time

def cunkuan(a):
	cunkuan=float(input("请输入存款金额："))
	if cunkuan<=0:
		print("输入错误！")

	else:
		a=a+cunkuan
		print("存款成功！存入：",cunkuan,"余额：",a)
	return a


def qukuan(b):
	c=float(input("请输入取款金额："))
	if c<=0:
		print("输入错误！")
	else:
		b=b-c
		print("取款成功！取出：",c,"余额：",b)
	return b



ka1="1001"
mima1="123456"
yue1=20000
ka2="1002"
mima2="123456"
yue2=15000
ka3="1003"
mima3="123456"
yue3=10000


print("欢迎来到python银行！")
cishu=0
while True:
	kahao=input("请输入卡号：")
	mima=input("请输入密码：")
	yue=0
	if kahao==ka1 and mima==mima1:
		yue=yue1
	elif kahao==ka2 and mima==mima2:
		yue=yue2
	elif kahao==ka3 and mima==mima3:
		yue=yue3
	else:
		cishu=cishu+1
		if cishu>=3:
			print("您已经3次输入错误，请联系银行柜台！")
			break
		else:
			print("卡号或密码第",cishu,"次输入有误，请重新输入！")
			continue
	#实现存取款业务的循环
	while True:
		xuanze=input("请输入要办理的业务：1.存款2.取款3.退卡")

		if xuanze=="1":
			yue=cunkuan(yue)#参数：余额  返回值：余额


			# cunkuan=float(input("请输入存款金额："))
			# if cunkuan<=0:
			# 	print("输入错误！")
			# 	continue
			# else:
			# 	yue=yue+cunkuan
			# 	print("存款成功！存入：",cunkuan,"余额：",yue)


		elif xuanze=="2":

			yue=qukuan(yue)#参数：余额  返回值：余额


			# qukuan=float(input("请输入取款金额："))
			# qukuan(yue,cunkuan)
			# if qukuan>yue:
			# 	print("余额不足！滚去赚钱！")
			# 	continue
			# else:
			# 	yue=yue-qukuan
			# 	print("取款成功！取了：",qukuan,"余额：",yue)


		elif xuanze=="3":
			print("操作结束，您的余额为：",yue)
			print("欢迎下次存钱！请收好卡片！")
			break
		else:
			print("没有这项业务，请重新选择！")
			continue
time.sleep(60)