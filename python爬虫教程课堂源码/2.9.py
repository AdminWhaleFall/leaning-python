from urllib import request
import random

#反爬虫2：判断请求来源的ip地址
#措施：使用代理IP

	

proxylist=[
	{"http":"182.111.64.7:41766"},
	{"http":"182.111.64.7:41766"},
	{"http":"182.111.64.7:41766"},
	{"http":"182.111.64.7:41766"},
	{"http":"182.111.64.7:41766"}
]

proxy=random.choice(proxylist)

print(proxy)


