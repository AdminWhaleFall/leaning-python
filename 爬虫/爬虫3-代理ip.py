from urllib import request
import random
#防爬虫2：判断请求来源的ip
#措施:使用代理ip叭
#免费的ip 收费的ip
# 47.103.11.171:80

proxylist=[
	{"http":"218.60.8.83:3129"},
]

proxy=random.choice(proxylist)

# 构建代理处理器对象
proxyHandler=request.ProxyHandler(proxy)

# 创建自定义opener
opener=request.build_opener(proxyHandler)

# 创建请求对象
req=request.Request("http://www.baidu.com/")

# 发送请求
data=opener.open(req)

print(data.read())




