'''
Author: WhaleFall
Date: 2021-02-02 14:24:41
LastEditTime: 2021-02-02 16:11:00
Description: OPQBot QQ机器人受到的信息保存到db数据库
'''
from botoy import *
import csv # 写入CSV文件
import codecs # 防止CSV乱码
import sys
path_py=sys.path[0]
import os
import time, datetime

def csvGroup(times,FromGroupName,FromGroupId,FromUserId,FromNickName,MsgType,Content,MsgRandom):
    # 以群号为单独一个CSV文件
    '''
    群名称,qq群号,QQ号,时间,qq群昵称,信息类型,信息,信息随机码
    '''
    # 构造
    dictData={
                "timeMsg":times,
                "FromUserId":FromUserId,
                "FromNickName":FromNickName,
                "MsgType":MsgType,
                "Content":Content,
                "MsgRandom":MsgRandom,
            }

    # 判断文件是否存在
    result=os.path.exists(r"{}//group//{} {}.csv".format(str(path_py),FromGroupId,FromGroupName))
    print(result)
    if result==False:
        # 如果不存在 则进行文件写入表头+内容
        with codecs.open(r"{}//group//{} {}.csv".format(str(path_py),FromGroupId,FromGroupName),"a",encoding="utf_8_sig") as f:
            headers = ["timeMsg","FromUserId","FromNickName","MsgType","Content","MsgRandom"]
            writer=csv.DictWriter(f,headers)
            writer.writeheader()
            
            writer.writerow(dictData)
    else:
        # 文件存在 则写入内容
        with codecs.open(r"{}//group//{} {}.csv".format(str(path_py),FromGroupId,FromGroupName),"a",encoding="utf_8_sig") as f:
            headers = ["timeMsg","FromUserId","FromNickName","MsgType","Content","MsgRandom"]
            writer=csv.DictWriter(f,headers)
            writer.writerow(dictData)
    print("写入成功!")


# bot函数
bot=Botoy(qq=2593923636,port=8888,host="http://192.168.101.4",log=True,log_file=False)

# 链接函数
@bot.when_connected
def _():
    print('连接成功啦~, 我只提醒你一次')

@bot.when_connected(every_time=True)
def _():
    print('连接成功啦~, 每次连接成功我都会提醒你')

# QQ群信息
@bot.on_group_msg
def group(ctx: GroupMsg):
    # print(ctx.Content)

    # 将时间戳变成时间格式
    timeArray = time.localtime(ctx.MsgTime)
    timemsg = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

    csvGroup(timemsg,ctx.FromGroupName,ctx.FromGroupId,ctx.FromUserId,ctx.FromNickName,ctx.MsgType,ctx.Content,ctx.MsgRandom)
    
    # if ctx.FromUserId != ctx.CurrentQQ and ctx.Content == 'test':
    #     print('ok')

# 好友信息
@bot.on_friend_msg
def friend(ctx: FriendMsg):
    print(ctx.Content)

# 警告信息
@bot.on_event
def event(ctx: EventMsg):
    print(ctx.Content)

if __name__ == '__main__':
    bot.run()