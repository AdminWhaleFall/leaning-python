from urllib import request
import random

#反爬虫2：判断请求来源的ip地址
#措施：使用代理IP

	

proxylist=[
	{"http":"101.248.64.82:80"}
]

proxy=random.choice(proxylist)

#构建代理处理器对象
proxyHandler=request.ProxyHandler(proxy)

#创建自定义opener
opener=request.build_opener(proxyHandler)

#创建请求对象
req=request.Request("http://www.baidu.com")

res=opener.open(req)

print(res.read())





