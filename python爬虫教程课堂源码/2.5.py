#伪装浏览器的爬虫
from urllib import request
import re

url=r"http://www.baidu.com/"

#构造请求头信息
header={
"User-Agent":"Mozilla/5.0 (Linux; U; An\
droid 8.1.0; zh-cn; BLA-AL00 Build/HUAW\
EIBLA-AL00) AppleWebKit/537.36 (KHTML, l\
ike Gecko) Version/4.0 Chrome/57.0.2987.13\
2 MQQBrowser/8.9 Mobile Safari/537.36"
}

#创建自定义请求对象  
#反爬虫机制1：判断用户是否是浏览器访问
#可以通过伪装浏览器进行访问
req=request.Request(url,headers=header)

#发送请求.获取响应信息
reponse=request.urlopen(req).read().decode() #解码---（编码encode()）

pat=r"<title>(.*?)</title>"

data=re.findall(pat,reponse)


print(data[0])

