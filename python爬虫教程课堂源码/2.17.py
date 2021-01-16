#2.15 实战：贴吧爬虫

from urllib import request
import urllib
import re

#构造请求头信息
header={
"User-Agent":"Mozilla/5.0 (Linux; U; An\
droid 8.1.0; zh-cn; BLA-AL00 Build/HUAW\
EIBLA-AL00) AppleWebKit/537.36 (KHTML, l\
ike Gecko) Version/4.0 Chrome/57.0.2987.13\
2 MQQBrowser/8.9 Mobile Safari/537.36"
}

url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

key="自学"

#post请求需要提交的参数
formdata={
	"i":key,
	"from":"AUTO",
	"to":"AUTO",
	"smartresult":"dict",
	"client":"fanyideskweb",
	"salt":"15503049709404",
	"sign":"3da914b136a37f75501f7f31b11e75fb",
	"ts":"1550304970940",
	"bv":"ab57a166e6a56368c9f95952de6192b5",
	"doctype":"json",
	"version":"2.1",
	"keyfrom":"fanyi.web",
	"action":"FY_BY_REALTIME",
	"typoResult":"false"
}

data=urllib.parse.urlencode(formdata).encode(encoding='utf-8')

req=request.Request(url,data=data,headers=header)

resp=request.urlopen(req).read().decode()

#正则表达式 提取"tgt":"和"}]]中间的任意内容
pat=r'"tgt":"(.*?)"}]]'

result=re.findall(pat,resp)

print(result[0])
