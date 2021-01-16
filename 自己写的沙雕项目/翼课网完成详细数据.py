'''
需求:1. 自动爬取学生完成数据,每60秒检查一次,自动刷新数据.
2. 若数据有变更对接iotqq发送群信息,发一封邮件
3. 若cookie失效则发送邮件与群信息,退出程序
4. 注意数据是多种形式的(作业,练习)
'''
import requests #爬虫模块
from fake_useragent import UserAgent #随机ua模块
import re
ua=UserAgent().random
cookie="bad_id5f0f07f0-f16d-11e8-8f8c-a91ca374c015=2095efc2-6c88-11e9-acac-513c32136d3b; _pk_ses.1.1d65=*; Hm_lvt_b4c8ad78a28febf2e2e8a8d38c14165f=1596100965; qimo_seosource_5f0f07f0-f16d-11e8-8f8c-a91ca374c015=%E7%AB%99%E5%86%85; qimo_seokeywords_5f0f07f0-f16d-11e8-8f8c-a91ca374c015=; href=https%3A%2F%2Fwww.ekwing.com%2Flogin%2Fview; accessId=5f0f07f0-f16d-11e8-8f8c-a91ca374c015; IS_SCHOOL_LOGIN=1; zg_did=%7B%22did%22%3A%20%221739f08dc50244-0ab4ba0e8e1de6-765c6203-15f900-1739f08dc513b7%22%7D; zg_373b07f02b874fcda2f678ece32d3cea=%7B%22sid%22%3A%201596101024856%2C%22updated%22%3A%201596101031300%2C%22info%22%3A%201596101024864%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22%E5%AD%A6%E7%94%9F%E7%AB%AF%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.ekwing.com%22%2C%22cuid%22%3A%20%226778866%22%7D; _pk_id.1.1d65=77e0fee674d6cfe1.1556766752.2.1596101033.1556767394.; Hm_lpvt_b4c8ad78a28febf2e2e8a8d38c14165f=1596101033; pageViewNum=5; EKWUID=fNjc3ODg2NiMjMTA3OTMwMDM5MCMjOTBjNzkwNTI3NzMzZTY1ODQyNzMxYmNlMzUzYmMxOGIjIzU5MmI4NjBkMjlkOGI0NjI2NzJlZDg3ZWExMDY2YmEzIyMxNTk2MTg3NDQzIyMxIyMyIyNla3dfc3R1ZGVudA%3D%3Dj"
url="https://www.ekwing.com/sysnotice/class"

#构造请求头
header={
	"UserAgent":ua,
	"Cookie":cookie,
	"Referer":"https://www.ekwing.com/",
	"Host":"www.ekwing.com",
}

#获取原始数据,传入第几页,1-10位学生
def GetList(page):

	#构造请求体
	datafrom={
		"page":page
	}
	global resp
	resp=requests.post(url,headers=header,data=datafrom).json()

#处理原始数据,获取每个学生的所有信息并输出用户详情 numm获取第几个学生
def GetOne(numm):

	numm=numm-1 #解决一下列表问题
	global content
	content=resp['data']['list'][numm]
	#用户详情
	user=content["user"]
	user_name=user["username"]  #姓名
	user_logo=user["logo"] #头像
	user_vip=user["vip"] #vip状态 返回的是布尔值不能与字符串拼接
	print("姓名:"+user_name+" vip状态:",user_vip)


#作业结果输出
def HwkResult():
	#作业类型 holiwork,college,"" 
	global content
	# print(content)
	module=content["module"]
	# print(module)

	if module=="holiwork":
		
		#holiwork类型 课内作业完成状态
		holiwork=content["cnt"] 

		holiwork_title=holiwork["title"] #标题 要用正则把“ ”拿出来
		pat_title='“(.*?)”'
		holiwork_title=re.findall(pat_title,holiwork_title)[0]

		holiwork_time=holiwork['duration'] #用时
		holiwork_score=holiwork["score"] #得分
		holiwork_total_score=holiwork["total_score"] #总分
		holiwork_finishTime=content["diff_times"] #提交时间

		print("作业:"+holiwork_title+"\n用时:"+holiwork_time+"\n得分:"+holiwork_score+"\n总分:"+holiwork_total_score+"\n提交时间:"+holiwork_finishTime)

	elif module=="college":
		#college类型 课外作业完成状态
		college=content['cnt']
		college_type=college['type'] #类型
		college_title=college['title'] #标题
		print("课外作业:"+college_type+"\n内容:"+college_title)

	else:
		# print("未知类型？")
		# 未知类型,可能是什么沙雕通知之类的叭
		nano=content["cnt"] 
		nano_title=nano["title"].strip()
		print("通知:"+nano_title)
		
GetList(1)
GetOne(2)
HwkResult()


