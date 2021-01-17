from OPQBot_hz import SendHz, SendLog
import re

key = "oC6UxXL8LoopDdZC0o"
aContent = "232hz15017662291"
# 抓取关键词hz后面的信息

hz = re.search(r'hz', str(aContent))
if hz == None:
    print("找不到关键词")

elif hz.group(0) == "hz":
    phote = re.search(r'1[35789]\d{9}$', str(aContent))

    if phote == None:
        print("手机号码不合法,不能玩弄八寻!生气ing")
        send(a.FromQQG, "手机号码不合法,不能玩弄八寻!生气ing", 2, a.FromQQ)
    else:
        phote1 = phote.group(0)
        print("手机号", phote1)

        sendStatus = SendHz(key, phote1)
        print(sendStatus)
        send(a.FromQQG, sendStatus, 2, a.FromQQ)
