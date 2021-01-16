from urllib import request

#构建处理器(请求头)对象(专门处理请求的对象)
http_hander=request.HTTPHandler()

#创建自定义opener
opener=request.build_opener(http_hander)

#创建自定义请求对象
req=request.Request("http://www.baidu.com")

#发送请求,获取响应
# reponse=opener.open(req).read()

#把自定义opener设置为全局 这样URLopen也会使用自定义的opener
request.install_opener(opener)

reponse=request.urlopen(req).read()

print(reponse.decode())