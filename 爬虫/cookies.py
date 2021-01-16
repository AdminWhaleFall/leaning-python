# cookie模拟登陆
from urllib import request
url = "http://i.baidu.com/"

#构造请求头信息 cookie加在请求头中 经过加密的
header={
	"User-Agent":"Mozilla/5.0 (Linux;\
	Android 8.0; Pixel 2 Build/OPD3.17\
	0816.012) AppleWebKit/537.36 (KHTML,like\
	Gecko) Chrome/69.0.3497.100 Mobi \
	le Safari/537.36",

	"Cookie":""
}

req=request.Request(url,headers=header)

rep=request.urlopen(req).read().decode()

print(rep)