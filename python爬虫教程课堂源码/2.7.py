#创建自定义opener
from urllib import request

#构建HTTP处理器对象（专门处理HTTP请求的对象）
http_hander=request.HTTPHandler()

#创建自定义opener
opener=request.build_opener(http_hander)

#创建自定义请求对象
req=request.Request("http://www.baidu.com")

#发送请求，获取响应
reponse=opener.open(req).read()

print(reponse)