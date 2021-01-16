# -*- coding:utf-8 -*-
# 有道翻译API
# post请求地址:http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule

from urllib import request
import urllib
import re # 正则表达式

#构造请求头信息
header={
	"User-Agent":"Mozilla/5.0 (Linux;\
	Android 8.0; Pixel 2 Build/OPD3.17\
	0816.012) AppleWebKit/537.36 (KHTML,like\
	Gecko) Chrome/69.0.3497.100 Mobi \
	le Safari/537.36"
}

# 把 _o 去掉 

url=r"http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

key="我喜欢黄颖怡"

# post请求需要提交的数据丫
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

# 整理post数据 调用 urllib 中的 parse 模块 进行 url encode 编码 再进行utf-8二进制编码
data=urllib.parse.urlencode(fromdata).encode(encoding="utf-8")

# 构造请求(request) data传则是post 不传则是get headers请求头信息
req=request.Request(url,data=data,headers=header)

# urlopen 导入构造请求后 发送请求 ; read读取后进行二进制转码再赋值给resp 响应信息(response)
resp=request.urlopen(req).read().decode()

# 响应信息是 json 格式  页面采用ajax无刷新请求(节约服务器资源)
print(resp)

#正则表达式 提取"tgt":"与"}]] 中间的任意内容
pat=r'"tgt":"(.*?)"}]]'

#结果 在response里面找pat正则表达式
result=re.findall(pat,resp)

# 返回是列表的格式 
print(result[0])







