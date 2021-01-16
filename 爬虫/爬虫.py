# 伪装浏览器的爬虫
from urllib import request
import re #正则表达式
import random #随机数模块
url=r"https://www.baidu.com/"

#手动创建自定义的请求对象
#反爬虫机制：1.判断用户是否是浏览器访问
#可以通过伪装浏览器[User-Agent]进行访问
#我的浏览器UA:
#Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36

#多个User-Agent
agent1 = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A372 MicroMessenger/7.0.10(0x17000a21) NetType/4G Language/zh_CN"
agent2 = "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.18 SP-engine/2.14.0 baiduboxapp/11.18.0.12 (Baidu; P1 8.1.0)"
agent3 = "Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; vivo Xplay6 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.8.5.1065 Mobile Safari/537.36"
agent4 = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
agent5 = "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)"

list1=[agent1,agent2,agent3,agent4,agent5] #UA放列表
agent=random.choice(list1) #随机选择列表里边的UA
print("UA:",agent)

#构造请求头信息 UA放入字典中 键对值 伪造手机UA 用 \连接不同行
header={
	"User-Agent":agent
}

# headers是固定的变量名 
req=request.Request(url,headers=header) #自定义UA对抗反扒机制


# 发送请求,获取响应信息 request自动创建请求对象
data=request.urlopen(req).read().decode()

# print(data)

pat=r"<title>(.*?)</title>" #数据清洗
title=re.findall(pat,data)

print(title[0])




'''
#解码decode()
print(data.decode())
# 类型是二进制bytes
print(type(data))
# 类型是字符串str
print(type(data.decode()))
'''
