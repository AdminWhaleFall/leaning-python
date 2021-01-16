from urllib import request
import urllib
# url中文编码 %E5%8C%97%21%21 #转码

wd={"wd":"北京"}

url="http://www.baidu.com/s?"

#构造url编码
wdd=urllib.parse.urlencode(wd)

url=url+wdd
print(url)

req=request.Request(url)

reponse=request.urlopen(req).read().decode()

print(reponse)







