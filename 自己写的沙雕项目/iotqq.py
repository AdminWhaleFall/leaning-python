import requests
import time

toUser=2734184475
botqq="2593923636"

#构造请求头信息
header={
	"User-Agent":"Mozilla/5.0 (Linux;\
	Android 8.0; Pixel 2 Build/OPD3.17\
	0816.012) AppleWebKit/537.36 (KHTML,like\
	Gecko) Chrome/69.0.3497.100 Mobi \
	le Safari/537.36"
}
#一言请求
y1_url="https://v1.hitokoto.cn"
resp=requests.get(y1_url,headers=header).json()
print(type(resp['from']))
y1=resp['hitokoto']+"《"+resp['from']+"》"+"————"+resp['from_who']
print(y1)

msg=y1
#构造post数据
fromdata={
"toUser":toUser,
"sendToType":1,
"sendMsgType":"TextMsg",
"content":msg,
"groupid":0,
"atUser":0,
}

#IoTQQ请求
url="http://192.168.101.4:8888/v1/LuaApiCaller?qq="+botqq+"&funcname=SendMsg&timeout=10"
# iotqq机器人在发送 post 请求时要传 json 数据
resp=requests.post(url,headers=header,json=fromdata).text
print("响应信息:",resp)




