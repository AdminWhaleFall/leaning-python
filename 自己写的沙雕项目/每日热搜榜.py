import requests
import json
from wordcloud import WordCloud
import sys
import datetime
import base64
import time

time = datetime.datetime.now().strftime('%Y-%m-%d %H时%M分%S秒')
print(time)

path = sys.path[0]

# 机器人配置信息
host = "192.168.101.4:8888"  # 服务器地址
bot_qq = "2593923636"

# api接口地址
api = "http://" + host + "/v1/LuaApiCaller"


def send_photo(toID, url):
    global time
    param = {
        'qq': bot_qq,  # bot的QQ
        'funcname': 'SendMsg'
    }

    datafrom = {
        "toUser": toID,  # 发到哪个QQ或者群号
        "sendToType": 2,  # 2发送给群 1发送给好友 3私聊
        "sendMsgType": "PicMsg",
        "content": "[PICFLAG]今日{}热点词云图已生成!".format(time),  # 要发送的文字内容
        # "groupid": 0,
        "atUser": 0,
        "picUrl": url,
        "picBase64Buf": "",
        "fileMd5": "",
        "PicPath": ""
    }
    header = {
        "Accept": "application/json",
    }
    try:
        resp = requests.post(url=api, params=param, data=json.dumps(datafrom), headers=header)
        if resp.json()["Ret"] != 0:
            print("发送有异常 接口响应:{}".format(resp.text))
            return "101"
        else:
            # print("发送成功~")
            return "200"
    except Exception as e:
        print("发送出现未知失败 错误:{} 响应:{}".format(e, "2"))
        return "0"


def draw(text):
    wordcloud = WordCloud(font_path="C:/Windows/Fonts/simyou.ttf",  # SIMYOU.TTF simkai.ttf
                          # background_color="white",
                          width=1080,
                          height=720,
                          max_font_size=80,
                          min_font_size=15,
                          # 词语水平方向排版出现的频率
                          prefer_horizontal=1,
                          random_state=30,
                          # 指定颜色
                          colormap="Paired",
                          # relative_scaling=True
                          # stopwords="我,的"
                          max_words=1000,
                          scale=2.0,
                          # stopwords=STOPWORDS.add('的')

                          ).generate(text)

    img = wordcloud.to_image()
    # print(img)
    wordcloud.to_file(r"{}//hot//{}百度热点词云图.jpg".format(path, time))
    wordcloud.to_file(r"{}//hot//new.jpg".format(path, time))
    img.show()


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
        return QQgroupList
    except Exception as e:
        print("请求群列表出现未知失败 错误:{} 响应:{}".format(e, resp.status_code))
        return "0"


# 图片上传图床
# def upload():
#     url = "https://my.qidian.com/ajax/headimage/uploadimg"
#     files = open("{}//hot//new.jpg".format(path), "rb")
#     resp = requests.post(url, files={"image": files})
#     print(resp.content.decode())


# upload()

url = "https://www.bjsoubang.com/api/getChannelData"

datafrom = json.dumps({
    "channel_id": "3",
})

header = {
    "Accept": "application/json",  # 协议规定 POST 提交必填
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "16",
    "Content-Type": "application/json;",
    "Host": "www.bjsoubang.com",
    "Origin": "https://www.bjsoubang.com",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same - origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}

try:
    resp = requests.post(url, headers=header, data=datafrom, )
    result = resp.json()
    list = result['info']['data']
    title_all = ""
    for content in list:
        # print(content)
        title = content['title']
        # print(title)
        title_all = title_all + title + ","
    print(title_all)
    draw(title_all)
except Exception as e:
    print("今日热点获取失败!{} http:{} {}".format(e, resp.status_code, resp))

# with open("{}//hot//new.jpg".format(path), "rb") as f:
#     img = f.read()
#     img_base64 = base64.b64encode(img).decode()
#     print(img_base64)
url = "http://127.0.0.1/hot/new.jpg"
GList = GetGroupList()
for Groupid in GList:
    send_photo(Groupid, url)
    time.sleep(5)