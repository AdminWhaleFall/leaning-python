from urllib import request

list1=[

"http://www.baidu.com",
"http://www.baidu.com",
"http://www.jiswiswissnduehduehd.com",
"http://www.baidu.com",
"http://www.baidu.com",

]

i=0
for url in list1:
	i=i+1
	
	try:
		request.urlopen(url)
		print("第",i,"次请求完成")
	except Exception as e:
		print(e)

	
