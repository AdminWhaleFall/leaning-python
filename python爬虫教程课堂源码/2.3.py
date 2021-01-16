#import urllib.request
from urllib import request
import re

url=r"http://www.baidu.com/"

Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE

#创建自定义请求对象  
#反爬虫机制1：判断用户是否是浏览器访问
#可以通过伪装浏览器进行访问
req=request.Request(url)

#发送请求.获取响应信息
reponse=request.urlopen(req).read().decode() #解码---（编码encode()）

pat=r"<title>(.*?)</title>"

data=re.findall(pat,reponse)


print(data[0])

