import requests
import re
#构造请求头信息
header={
	"User-Agent":"Mozilla/5.0 (Linux;\
	Android 8.0; Pixel 2 Build/OPD3.17\
	0816.012) AppleWebKit/537.36 (KHTML,like\
	Gecko) Chrome/69.0.3497.100 Mobi \
	le Safari/537.36"
}

key="我喜欢她"
#post提交的数据
fromdata={
	"i":key,
	"from":"AUTO",
	"to":"AUTO",
	"smartresult":"dict",
	"client":"fanyideskweb",
	"salt":"15957393890103",
	"sign":"d411668fd81f79fdf349d8b2bbe815cd",
	"ts":"1595739389010",
	"bv":"7aafb7b8528c5bc925fc8aea94e3c5e2",
	"doctype":"json",
	"version":"2.1",
	"keyfrom":"fanyi.web",
	"action":"FY_BY_CLICKBUTTION",
}

url=r"http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

# 请求头信息:headers ; post提交数据:data ; get提交数据:params=wd
resp=requests.post(url,headers=header,data=fromdata)

'''
#解析为字符串
print(resp.text)
#解析为二进制再转码
print(resp.content.decode())
'''

# 调用json()方法 自动解析成json格式-->字典
print(resp.json())

# print(resp.text)
pat=r'"tgt":"(.*?)"}]]'
result=re.findall(pat,resp.text)
print(result[0])










