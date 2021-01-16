#import urllib.request
from urllib import request

url=r"http://www.baidu.com/"

#发送请求.获取响应信息
reponse=request.urlopen(url).read()


print(type(reponse))

