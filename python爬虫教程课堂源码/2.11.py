#2.11 处理get请求

from urllib import request
import urllib
#http://www.baidu.com/s?wd=%E5%8C%97%E4%BA%AC #url编码

wd={"wd":"北京"}

url="http://www.baidu.com/s?"

#构造url编码
wdd=urllib.parse.urlencode(wd)

url=url+wdd

req=request.Request(url)

reponse=request.urlopen(req).read().decode()

print(reponse)








