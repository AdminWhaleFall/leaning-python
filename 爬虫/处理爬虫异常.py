from urllib import request
import urllib

list1=[
"http://www.baidu.com",
"http://www.baidu.com",
"http://www.baidu.com",
"http://www.baidu.com",
"http://www.ba32132idu.com",
]

i=0
for url in list1: #for循环遍历列表
	# print(url)
	i=i+1
	try:
		request.urlopen(url)
		print("第",i,"次请求完成")
	except Exception as e:
		print("请求错误:",e)







