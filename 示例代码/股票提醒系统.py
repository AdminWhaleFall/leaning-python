#股票提醒系统 tushare

import tushare
import time
import smtplib
from email.mime.text import MIMEText

#获取股票数据
def getrealtimedata(share):
	dataNow=tushare.get_realtime_quotes(share.code)
	share.name=dataNow.loc[0][0]
	share.price=float(dataNow.loc[0][3])
	share.high=dataNow.loc[0][4]
	share.low=dataNow.loc[0][5]
	share.volumn=dataNow.loc[0][8]
	share.amount=dataNow.loc[0][9]
	share.openToday=dataNow.loc[0][1]
	share.pre_close=dataNow.loc[0][2]
	share.timee=dataNow.loc[0][30]
	share.describe="股票名："+share.name+"当前价格："+str(share.price)

	return share

#发送邮件
def sendemail(subject,content):
	msg_from="test666@126.com" #发送方
	pwd="12344321a"#授权码
	to="2274986616@qq.com"

	#构造邮件
	msg=MIMEText(content) #msg邮件对象
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

#股票类
class Share():
	def __init__(self,code,buy,sale):
		self.name=""
		self.price=""
		self.high=""
		self.low=""
		self.volumn=""
		self.amount=""
		self.openToday=""
		self.pre_close=""
		self.timee=""
		self.describe=""
		self.code=code
		self.buy=buy
		self.sale=sale



def main(shareList):

	for share in shareList:
		sss=getrealtimedata(share)

		print(sss.describe)

		if sss.price<=sss.buy:
			print("达到买点，如果有钱请赶紧买！")
			sendemail("达到买点",sss.describe)
		elif sss.price>=sss.sale:
			print("达到卖点，手里有货的话赶紧卖！")
			sendemail("达到卖点",sss.describe)
		else:
			print("别买也别卖，等着！")


while 1==1:

	share1=Share("600106",3.1,3.18)
	share2=Share("601988",3.4,3.5)
	share3=Share("000591",3.0,3.7)

	list1=[share1,share2,share3]
	print("-----------")
	main(list1)

	time.sleep(600)




		
		





		