import requests

# opqbot设置
botID = "2593923636"
botUrl = "http://192.168.101.4:8888"

# 必应接口
url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
header = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; EVA-AL10 Build/HUAWEIEVA-AL10;\
		 wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89\
		  Mobile Safari/537.36 T7/11.20 SP-engine/2.16.0 baiduboxapp/11.20.0.14 (Baidu; P1 8.0.0)",
}

resp = requests.get(url=url, headers=header).json()

# print(resp)
# 获取图片描述
title = resp['images'][0]['copyright']
print(title)

# 获取图片链接 要拼接bing.com
images_url = "https://bing.com" + resp['images'][0]['url']
print(images_url)


def sendGroup(GroupId, content, picUrl):
    url = botUrl + "/v1/LuaApiCaller?qq=" + botID + "&funcname=SendMsg&timeout=10"
    datafrom = {
        "toUser": GroupId,
        "sendToType": 2,
        "sendMsgType": "PicMsg",
        "content": content,
        "groupid": 0,
        "atUser": 0,
        "picUrl": picUrl,
        "picBase64Buf": "",
        "fileMd5": ""

    }

    resp = requests.post(url=url, json=datafrom)
    print(resp.text)
    print(str(resp.elapsed.total_seconds()) + "s")


sendGroup("1146569665", "[PICFLAG]bing每日一图:\n" + title, images_url)
