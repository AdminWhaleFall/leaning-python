#coding=utf-8
import socketio
import json
import requests
import pdb
import re
import logging
import time
import socket
from OPQBot_hz import SendHz,SendLog #自用轰炸机函数
key="oC6UxXL8LoopDdZC0o"
'''
Python插件SDK Ver 0.0.1
维护者:enjoy(2435932516)
有问题联系我。
'''
robotqq = "2593923636" #机器人QQ号
webapi = "http://192.168.101.4:8888" #Webapi接口 http://127.0.0.1:8888
sio = socketio.Client()
#log文件处理
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',level=0,filename='new.log',filemode='a')

class GMess:
    #QQ群消息类型
    def __init__(self,message1):
        #print(message1)
        self.FromQQG = message1['FromGroupId'] #来源QQ群
        self.QQGName = message1['FromGroupName'] #来源QQ群昵称
        self.FromQQ = message1['FromUserId'] #来源QQ
        self.FromQQName = message1['FromNickName'] #来源QQ名称
        self.Content = message1['Content'] #消息内容

def send(ToQQ,Content,sendToType,atuser=0,sendMsgType='TextMsg',groupid=0):
    tmp={}
    tmp['sendToType'] = sendToType
    tmp['toUser']= ToQQ
    tmp['sendMsgType']=sendMsgType
    tmp['content']=Content
    tmp['groupid']=0
    tmp['atUser']=atuser
    tmp1 = json.dumps(tmp)
    requests.post(webapi+'/v1/LuaApiCaller?funcname=SendMsg&qq='+robotqq,data=tmp1)
def sendPic(ToQQ,Content,sendToType,imageUrl):
    tmp={}
    tmp['sendToType'] = sendToType
    tmp['toUser']= ToQQ
    tmp['sendMsgType']="PicMsg"
    tmp['content']=Content
    tmp['picBase64Buf']=''
    tmp['fileMd5']=''
    tmp['picUrl']=imageUrl
    #转化为json
    tmp1 = json.dumps(tmp)
    #print(tmp1)
    print(requests.post(webapi+'/v1/LuaApiCaller?funcname=SendMsg&timeout=10&qq='+robotqq,data=tmp1).text)
 
class Mess:
    def __init__(self,message1):
        self.FromQQ = message1['ToUin']
        self.ToQQ = message1['FromUin']
        self.Content = message1['Content']
# standard Python
 
# SocketIO Client
#sio = socketio.AsyncClient(logger=True, engineio_logger=True)
 
# ----------------------------------------------------- 
# Socketio
# ----------------------------------------------------- 
def beat():
    while(1):
        sio.emit('GetWebConn',robotqq)
        time.sleep(60) #心跳包连接
 
@sio.event
def connect():
    print('服务器连接成功！')
#
    sio.emit('GetWebConn',robotqq)#取得当前已经登录的QQ链接
    beat() #心跳包，保持对服务器的连接
 
@sio.on('OnGroupMsgs')
def OnGroupMsgs(message):
    ''' 监听群组消息'''
    tmp1 = message
    tmp2 = tmp1['CurrentPacket']
    tmp3 = tmp2['Data']
    a = GMess(tmp3)
    cm = a.Content.split(' ',3) #分割命令
    '''
    a.FrQQ 消息来源
    a.QQGName 来源QQ群昵称
    a.FromQQG 来源QQ群
    a.FromNickName 来源QQ昵称
    a.Content 消息内容
    '''
    print(a.Content)
    # if a.Content=='#菜单':
    #     #print(a.ToQQ)
    #     send(a.FromQQG,"功能",2,a.FromQQ)

    # hz=re.search(r'hz',str(a.Content))
    # print(hz)
    # if hz==None:
    #     print(a.Content)
    # # elif hz.group(0)=="hz":
    # else:
    #     phote=re.search(r'1[35789]\d{9}$',str(a.Content))
    #     if phote==None:
    #         print("手机号码不合法,不能玩弄八寻!生气ing")
    #         send(a.FromQQG,"手机号码不合法,不能玩弄八寻!生气ing",2,a.FromQQ)
    #     else:
    #         phote1=phote.group(0)
    #         print("手机号",phote1)
    #         sendStatus=SendHz(key,phote1)
    #         print(sendStatus)
    #         send(a.FromQQG,sendStatus,2,a.FromQQ)
        

    # if a.Content=='111':
    #     sendResult=SendLog(key)
    #     send(a.FromQQG,sendResult,2,a.FromQQ)
        

    te = re.search(r'\#(.*?)',str(a.Content))
    if te == None:
    	return
    print(te.group(0))
    SendHz(key,te.group(0))
    # temp = eval(requests.get("https://hlqsc.cn/lexicon/?id="+str(a.FromQQ)+"&msg="+te.group(1)+"&name=tuling").text)
    # sendtext = re.sub(r"http.*", "", temp['text'], count=0, flags=0)
    # send(a.FromQQG,sendtext,2,a.FromQQ)
    # logging.info("["+str(a.FromQQG)+']'+str(a.FromQQ)+": "+str(a.Content))
    #print(message)
    

@sio.on('OnFriendMsgs')
def OnFriendMsgs(message):
    ''' 监听好友消息 '''
    tmp1 = message
    tmp2 = tmp1['CurrentPacket']
    tmp3 = tmp2['Data']
    a = Mess(tmp3)
    #print(tmp3)
    cm = a.Content.split(' ')
    if a.Content=='#菜单':
        send(a.ToQQ,"你好",1)
    
@sio.on('OnEvents')
def OnEvents(message): #杂七杂八的事件
    ''' 监听相关事件'''
    print(message)   
# ----------------------------------------------------- 
def main():
    try:
        sio.connect(webapi,transports=['websocket'])
        #pdb.set_trace() 这是断点
        sio.wait()
    except BaseException as e:
        logging.info(e)
        print (e)
 
if __name__ == '__main__':
   main()