import requests
import xlrd
import time

def name(name):
	
	url="http://tool.rrbrr.com/index/guessGender"
	datafrom={
		"kw":name
	}
	try:
		resp=requests.get(url=url,params=datafrom)
		resp=resp.json()
	except Exception as e:
		
		content="json化出错，可能是请求过频繁:"+str(resp.status_code)
		return "！出错！",content
	

	#查询的名字 若找不着名字处理异常
	try:
		checkName=resp["data"]["name"]
		gender=resp["data"]["gender"]
	except Exception as e:
		checkName="你确定是人的名字？"
		gender="异常"
	#性别 0:女孩纸 1:男孩子 "异常":名字不存在
	if gender=="1":
		gender="男孩子"
	elif gender=="0":
		gender="女孩纸"
	else:
		gender="？不明生物？"
	#性别权重百分比
	male_percentage=str(resp["data"]["male_percentage"])+"%" #男性
	female_percentage=str(resp["data"]["female_percentage"])+"%" #女性
	#同名人数
	total=str(resp["data"]["total"])
	total_percentage=resp["data"]["total_percentage"]

	gender_all=" 性别:"+gender+"\n男孩子概率:"+male_percentage+" 女孩纸概率:"+female_percentage
	total_all="你的名字是"+total_percentage+"里挑一,"+"同名人数："+total

	#玄学测运
	tiangee=resp["data"]["score"]["tiangee"]["yy"] #天格
	digee=resp["data"]["score"]["digee"]["yy"] #地格
	waigearr=resp["data"]["score"]["waigearr"]["yy"] #外格
	zonggearr=resp["data"]["score"]["zonggearr"]["yy"] #总格
	rssancai=resp["data"]["score"]["rssancai"]["yy"].replace('\r\n','') #总结

	gender="查询名字:"+checkName+gender_all+"\n"+total_all
	minyun="天格:"+tiangee+"\n"+"地格:"+digee+"\n"+"外格:"+waigearr+"\n"+"总格:"+zonggearr+"\n"+"总结:"+rssancai

	return gender,minyun

gender,minyun=name("张广平")
print(gender+"\n--------------------\n"+minyun)

# data=xlrd.open_workbook('D:\\test.xls')
# sheet=data.sheets()[0]
# nameList=sheet.col_values(3)
# # print(name)
# for n in nameList:
# 	gender,minyun=name(n)
# 	c="提取到的名字："+n+"\n"+gender+"\n------------------------------------\n"
# 	print(c)
# 	with open(r"C:\Users\27341\Desktop\name.txt","a") as f:
# 		f.write(c)



