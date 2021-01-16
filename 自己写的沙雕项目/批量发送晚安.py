# IoTQQ好友发送晚安
import requests
import time

iotqq="2593923636"

#获取好友列表
url_friendlist="http://192.168.101.4:8888/v1/LuaApiCaller?qq="+iotqq+"&funcname=GetQQUserList&timeout=10"
# 发送好友信息
url_send="http://192.168.101.4:8888/v1/LuaApiCaller?qq="+iotqq+"&funcname=SendMsg&timeout=10"

#获取好友列表
# post请求数据
data_getlist={
  "StartIndex":0
}

GetQQUserList=requests.post(url_friendlist,json=data_getlist).json()
# print(GetQQUserList)
#读取好友列表
Friendlist=GetQQUserList['Friendlist']
# print(Friendlist)

#读取好友个数
Friend_count=GetQQUserList['Friend_count']

# 用for循环遍历数组读取QQ号
Friend_qq=[]
for i in Friendlist:
	qq=i['FriendUin']
	# print(qq)
	Friend_qq.append(qq)

print(Friend_qq)



