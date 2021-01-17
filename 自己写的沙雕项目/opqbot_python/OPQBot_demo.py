# OPQBot QQ机器人接口
import requests
import json
from time import *

# 机器人配置信息
host = "192.168.101.4:8888"  # 服务器地址
bot_qq = "2593923636"

# api接口地址
api = "http://" + host + "/v1/LuaApiCaller"


# 发送 群聊\好友 文字信息
def send_txt(ty, toID, content):
    param = {
        'qq': bot_qq,  # bot的QQ
        'funcname': 'SendMsg'
    }

    datafrom = {
        "toUser": toID,  # 发到哪个QQ或者群号
        "sendToType": ty,  # 2发送给群 1发送给好友 3私聊
        "sendMsgType": "TextMsg",
        "content": content,  # 要发送的文字内容
        "groupid": 0,  # 群号
    }
    try:
        resp = requests.post(url=api, params=param, data=json.dumps(datafrom))
        if resp.json()["Ret"] != 0:
            print("发送有异常 接口响应:{}".format(resp.text))
            return "101"
        else:
            # print("发送成功~")
            return "200"
    except Exception as e:
        print("发送出现未知失败 错误:{} 响应:{}".format(e, resp.status_code))
        return "0"


# 获取bot加入的群列表
def GetGroupList():
    param = {
        'qq': bot_qq,  # bot的QQ
        'funcname': 'GetGroupList'
    }
    datafrom = {
        "NextToken": ""
    }

    try:
        resp = requests.post(url=api, params=param, data=json.dumps(datafrom))
        TroopList = resp.json()["TroopList"]
        QQgroupList = []
        QQgroupList_all = []
        for QQgroup in TroopList:
            # print(QQgroup)
            groupID = QQgroup['GroupId']
            groupName = QQgroup['GroupName']
            group = {"groupID": groupID, "groupName": groupName}
            QQgroupList.append(groupID)
            QQgroupList_all.append(group)
        print("获取到的QQ群列表:", QQgroupList)
        # print("详细信息:", QQgroupList_all)
        return QQgroupList_all
    except Exception as e:
        print("请求群列表出现未知失败 错误:{} 响应:{}".format(e, resp.status_code))
        return "0"


# 获取指定群里边的群员
def GetGroupUserList(groupID):
    param = {
        'qq': bot_qq,  # bot的QQ
        'funcname': 'GetGroupUserList'
    }

    datafrom = {
        "GroupUin": groupID,
        "LastUin": 0
    }
    try:
        resp = requests.post(url=api, params=param, data=json.dumps(datafrom))
        count = resp.json()["Count"]  # 人数
        MemberList = resp.json()['MemberList']
        groupMemberList = []
        for Member in MemberList:
            age = Member['Age']
            qqid = Member['MemberUin']  # QQ号
            qqname = Member['NickName']  # QQ昵称
            groupMember = {"name": qqname, "id": qqid, "age": age}
            groupMemberList.append(groupMember)
        # print("群:{} 的{}位群成员:{}".format(groupID, count, groupMemberList))
        return count, groupMemberList
    except Exception as e:
        print("获取群成员列表未知失败 错误:{} 响应:{}".format(e, resp.status_code))
        return "0", "0"


# GetGroupUserList(1028871825)

if __name__ == "__main__":
    GroupList = GetGroupList()
    #
    for Group in GroupList:
        GroupID = Group['groupID']
        GroupName = Group['groupName']

        # 获取群成员
        count, GroupMember = GetGroupUserList(GroupID)
        age = 0
        for user in GroupMember:
            # print(user)
            age_p = user['age']

            age = age_p + int(age)
        # print(age)
        evel_age = str(age / count)
        content = "群:{}({}) 共有{}人 平均年龄:{}".format(GroupName, GroupID, count, evel_age)
        print(content)
        # status = send_txt(2, GroupID, content)
        # if status == "200":
        #     print("群{}({}) 发送成功".format(GroupName, GroupID))
        #
        # sleep(5)
