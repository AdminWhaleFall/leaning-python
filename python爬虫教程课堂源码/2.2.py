#import urllib.request
from urllib import request
import re

url=r"http://www.baidu.com/"

#发送请求.获取响应信息
reponse=request.urlopen(url).read().decode() #解码---（编码encode()）

pat=r"<title>(.*?)</title>"

data=re.findall(pat,reponse)


print(data)

