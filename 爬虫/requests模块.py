# requests 模块
import requests

# 获取响应信息 http状态码 以文本的方式获取.text(会乱码) 以二进制的形式获取 .content
# .decode() 进行二进制转码
response=requests.get("http://www.baidu.com").content.decode()
# 方法二
response=requests.request("get","http://www.baidu.com").content.decode()

#requests 模块添加请求头和参数

#构造请求头信息
header={
	"User-Agent":"Mozilla/5.0 (Linux;\
	Android 8.0; Pixel 2 Build/OPD3.17\
	0816.012) AppleWebKit/537.36 (KHTML,like\
	Gecko) Chrome/69.0.3497.100 Mobi \
	le Safari/537.36"
}

wd={"wd":"中国"}
# 不需要
# 整理post数据 调用 urllib 中的 parse 模块 进行 url encode 编码 再进行utf-8二进制编码
#data=urllib.parse.urlencode(fromdata).encode(encoding="utf-8")

# 自动创建 发送请求, params:参数个数 自动编码 header:请求头
rep=requests.get("http://www.baidu.com/s?",params=wd,headers=header)

data=rep.text  #返回一个字符串类型的数据
data2=rep.content #返回二进制形式的数据 中文-->\xe9\x97\xae 含有图片音频
# de:解码 en:编码 
print(data2.decode())





