# 潮汐每日一句 发布+采集
import requests
import time

requests.packages.urllib3.disable_warnings()


# 获取潮汐日贴
def GetJuzhi():
    # 时间格式化输出
    time_day = time.strftime("%Y-%m-%d")
    url = "https://tide-api.moreless.io/v1/dailypics?from=" + time_day + "&to=" + time_day
    header = {
        "Accept-Language": "zh-CN",
        "User-Agent": "TideAndroid/3.8.0 (Linux; Android 6.0.1; MuMu Build/eng.luoweiqiao.20200917.180925) okhttp/4.5.0",
        "ML-AppID": "2",
        "ML-AppVersion": "3.8.0",
        "ML-VersionCode": "1313",
        "ML-DeviceID": "210435ca45b2e72c",
        "ML-DeviceProductID": "x86",
        "ML-SystemVersion": "6.0.1",
        "ML-SystemLanguage": "zh",
        "ML-SystemRegion": "CN",
        "ML-Carrier": "MC0w",
        "ML-NetworkStatus": "wifi",
        "Accept-Encoding": "gzip",
        "ML-Authorization": "VLcSl5MPn7F2YVeU37x8tqXs3mQ=",
        "ML-Timestamp": str(int(time.time())),
        "Host": "tide-api.moreless.io",
        "Connection": "Keep-Alive",
    }

    resp = requests.get(url, headers=header, verify=False).json()
    pic_url = resp[0]['pic_url']
    author = resp[0]['content']['zh-Hans']['author_title']['text'] + "," + resp[0]['content']['zh-Hans']['author'][
        'text']
    content = resp[0]['content']['zh-Hans']['quote']['text']

    return content, author, pic_url


# xnote网络记事本留言板
def SendXnote(username, content):
    try:
        url = "http://www.xnote.cn/api/feedback/save/"
        header = {
            "Accept": "application/json, text/javascript, */*",
            "Referer": "http://www.xnote.cn/feedback/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        }
        datafrom = {
            "username": username,
            "content": content,
            "id": "",
        }
        resp = requests.post(url, headers=header, data=datafrom).json()
        if resp["success"] == True:
            print("[Success]Xnote留言板发送成功!")
        else:
            print("[Error]Xnote留言板发送失败!", resp)
    except Exception as e:
        print("[Error]Xnote留言板发送出现未知错误", e)


# SendXnote("administartor", "谢谢大家的支持,我们要整改了!")

content, author, pic_url = GetJuzhi()
strr = content+"———"+author
print("[Success]"+strr)
SendXnote("潮汐一言", strr)
