# coding=utf-8
'''
需求:1. 自动爬取学生完成数据,每60秒检查一次,自动刷新数据.
2. 若数据有变更对接iotqq发送群信息,发一封邮件
3. 若cookie失效则发送邮件与群信息,退出程序
4. 注意数据是多种形式的(作业,练习)
'''
import requests  # 爬虫模块
from fake_useragent import UserAgent  # 随机ua模块
import re
# from bs4 import BeautifulSoup
import time
from lxml import etree
# 支持邮件发送的模块
import smtplib
from email.mime.text import MIMEText
# 获取时间
import datetime

ua = UserAgent().random
# cookie 24小时保护期
cookie = "IS_SCHOOL_LOGIN=1; zg_did=%7B%22did%22%3A%20%221738f42230516f-0fb5fcdda7ceab-7d56670e-15f900-1738f4223061a0%22%7D; Hm_lvt_b4c8ad78a28febf2e2e8a8d38c14165f=1595836285,1595930914,1596100761; href=https%3A%2F%2Fwww.ekwing.com%2Flogin%2Fview%3Fhref%3Dhttps%253A%252F%252Fwww.ekwing.com%252FHome%252Findex; accessId=5f0f07f0-f16d-11e8-8f8c-a91ca374c015; Hm_lvt_70b7d1f99329b1ded9b60564cd0c45f6=1595838359,1595930912,1596100757,1596188160; uid=nk4%2BKhMYXrGjNiP8hnKR1aKpetMFtlNaTQiDip52duU%3D; _pk_ses.1.1d65=*; qimo_seosource_5f0f07f0-f16d-11e8-8f8c-a91ca374c015=%E7%AB%99%E5%86%85; qimo_seokeywords_5f0f07f0-f16d-11e8-8f8c-a91ca374c015=; zg_373b07f02b874fcda2f678ece32d3cea=%7B%22sid%22%3A%201596195207695%2C%22updated%22%3A%201596195218555%2C%22info%22%3A%201595836343057%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22%E5%AD%A6%E7%94%9F%E7%AB%AF%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.ekwing.com%22%2C%22cuid%22%3A%20%226778866%22%7D; _pk_id.1.1d65=e9ec584ca2083854.1595836285.6.1596196283.1596188193.; Hm_lpvt_b4c8ad78a28febf2e2e8a8d38c14165f=1596196283; Hm_lpvt_70b7d1f99329b1ded9b60564cd0c45f6=1596196283; pageViewNum=10; EKWUID=ZNjc3ODg2NiMjMTA3OTMwMDM5MCMjOTBjNzkwNTI3NzMzZTY1ODQyNzMxYmNlMzUzYmMxOGIjI2EyYjUzM2MxNDk4MjcwNjFjMTYxZWEyZTYxZDI5N2QyIyMxNTk2MjgyNjk0IyMxIyMyIyNla3dfc3R1ZGVudA%3D%3D2"
url = "https://www.ekwing.com/sysnotice/class"  # 练习情况数据主接口
url_index = "https://www.ekwing.com/Home/index"  # 主页 用于获取个人信息
iotqq_url = "http://192.168.101.4:8888"  # iotqq机器人地址
iotqq = "2593923636"  # iotqq机器人账号
# 配置邮件发送参数(请到email_send函数配置)


# 构造请求头
header = {
    "UserAgent": ua,
    "Cookie": cookie,
    "Referer": "https://www.ekwing.com/",
    "Host": "www.ekwing.com",
}


# 获取原始数据,传入第几页,每页1-10位学生;并检查cookie有效度
def GetList(page):
    # 构造请求体
    datafrom = {
        "page": page
    }
    global resp
    try:
        resp = requests.post(url, headers=header, data=datafrom).json()  # 如果cookie失效 json化也会失败的叭
    except Exception as e:
        time2 = datetime.datetime.now()
        UpdateTime = time2.strftime('%Y-%m-%d %H:%M:%S')
        print("请更新cookie！将发送提醒! 时间:" + UpdateTime)
        # email_send("2734184475@qq.com","请到服务器更新翼课网cookie!并重启程序!\n时间:"+UpdateTime)
        iotqq_send(1, 2734184475, "八寻宁宁提醒您,请到服务器更新翼课网cookie!并重启程序!\n时间:" + UpdateTime)
        raise e  # 抛出异常 退出程序


# 获取登陆者个人信息
def GetLogin():
    # 直接从接口获取 接收员信息
    try:
        global receive
        receive = resp['data']['list'][0]  # 取当前第一个学生叭
        receive_name = receive["receive_name"]  # 姓名
        receive_vip = str(receive["self_vip"])  # 是否为vip 返回的是布尔值

        receive_all = "cookie登录姓名:" + receive_name + "\nvip状态:" + receive_vip

        # 简单的从主页获取
        index = requests.get(url_index, headers=header).content.decode()
        IndexHtml = etree.HTML(index)  # 序列化html
        html = etree.tostring(IndexHtml, encoding="utf-8").decode()  # 页面的完整html
        # print(html)
        unFinish_homework = IndexHtml.xpath("//span[@class='text_emphasis']")[0].text  # 未完成的作业
        unFinish_text = IndexHtml.xpath("//span[@class='text_emphasis']")[1].text  # 未完成的考试

        unFinish_all = "\n未完成作业:" + unFinish_homework + "\n未完成考试:" + unFinish_text
        global receiveX
        receiveX = receive_all + unFinish_all
    except Exception as e:  # 如果出现错误则运行以下语句
        print("读取用户信息出现异常", e)


# 处理原始数据,获取每个学生的所有信息并输出用户详情 numm获取第几个学生
def GetOne(numm):
    numm = numm - 1  # 解决一下列表问题
    global content
    content = resp['data']['list'][numm]
    # 用户详情
    user = content["user"]
    user_name = user["username"]  # 姓名
    user_logo = user["logo"]  # 头像
    user_vip = str(user["vip"])  # vip状态 返回的是布尔值 结果已转换
    global user_all
    user_all = "姓名:" + user_name + " vip状态:" + (user_vip)  # 用户详细信息
    return user_name


# 作业结果输出
def HwkResult():
    # 作业类型 holiwork,college,""
    global content
    # print(content)
    module = content["module"]
    # print(module)

    # holiwork:假期作业(总分是str类型) homework:平时作业(总分是int类型) 尝试合并一下
    if module == "holiwork" or module == "homework":

        # holiwork类型 课内作业完成状态
        holiwork = content["cnt"]
        # print(holiwork)
        holiwork_title = holiwork["title"]  # 标题 要用正则把“ ”拿出来
        pat_title = '“(.*?)”'
        holiwork_title = re.findall(pat_title, holiwork_title)[0]

        holiwork_time = holiwork['duration']  # 用时
        holiwork_score = holiwork["score"]  # 得分
        holiwork_total_score = str(holiwork["total_score"])  # 总分 直接转为str
        holiwork_finishTime = content["diff_times"]  # 提交时间
        global hwk_all
        hwk_all = "作业:" + holiwork_title + \
                  "\n用时:" + holiwork_time + "\n得分:" \
                  + holiwork_score + "\n总分:" + holiwork_total_score + \
                  "\n提交时间:" + holiwork_finishTime
        return hwk_all
    # print(hwk_all)

    elif module == "college":
        # college类型 课外作业完成状态
        college = content['cnt']
        college_type = college['type']  # 类型
        college_title = college['title']  # 标题
        global college_all
        college_all = "课外作业:" + college_type + "\n内容:" + college_title
        return college_all
    # print(college_all)

    else:
        # print("未知类型？")
        # 未知类型,可能是什么沙雕通知之类的叭
        nano = content["cnt"]
        nano_title = nano["title"].strip()
        global nano_all
        nano_all = "通知:" + nano_title
        return nano_all
    # print(nano_all)


# 对接IoTQQ sendToType:1好友 2群 3私聊 整数型
def iotqq_send(sendToType, toUser, content):
    iotqq_sendURL = iotqq_url + "/v1/LuaApiCaller?qq=" + iotqq + "&funcname=SendMsg&timeout=10"

    datafrom = {
        "toUser": toUser,  # 群号或好友
        "sendToType": sendToType,  # 1好友 2群 3私聊
        "sendMsgType": "TextMsg",  # 发送的类型
        "content": content,  # 发送内容
        "groupid": 0,  # 除了私聊 外其他情况为0
        "atUser": 0,  # @的对象
    }

    try:
        QQRep = requests.post(url=iotqq_sendURL, json=datafrom).json()
    except Exception as ex:
        print("请求iotqq时出现错误:", ex)

    if QQRep['Ret'] == 0:
        print("QQ信息发送成功啦")
    else:
        print("QQ信息发送失败,请检查IoTQQ")


# 对接邮箱发送
def email_send(email_to, email_content):
    msg_from = "whalefall2020@163.com"  # 发送方
    pwd = "BFEPKZGIINCMBEGM"  # 授权密码
    to = email_to  # 接收方

    subject = "丫翼课网小爬虫丫"  # 主题
    # 文本 支持HTML 需修改构造邮件参数
    content = email_content

    # 构造邮件 支持HTML 传入以下参数
    msg = MIMEText(content, "html", "utf-8")  # msg邮件对象
    # 邮件中的构造跟字典类似,把subject赋值给msg字典中的Subject键
    msg["Subject"] = subject  # 主题
    msg["From"] = msg_from
    msg["To"] = to

    try:
        ss = smtplib.SMTP_SSL('smtp.163.com', 994)  # smtp服务器地址
        ss.login(msg_from, pwd)  # 登录 账号,密码
        # 发送邮件 发送方 接收方 内容(灵活转码)
        ss.sendmail(msg_from, to, msg.as_string())
    except Exception as e:
        print("邮箱发送出现错误:", e)
    else:
        print("邮件发送应该成功了叭")


# email_send("huangjiale2019@gmail.com","翼课网小爬虫测试")

# iotqq_send(1,2734184475,"测试好友")
# iotqq_send(2,1038347983,"测试群聊")

time4 = datetime.datetime.now()
startTime = time4.strftime('%Y-%m-%d %H:%M:%S')
print("程序开始时间:", startTime)

GetList(1)
GetLogin()
res = ""
for x in range(1, 11):
    uers = GetOne(x)
    ret = HwkResult()
    res = res + user_all + "\n" + ret + "\n------------------------\n"

send = "初始化完成,开始运行时间:" + startTime + "\n" + receiveX + "\n------------------------\n" + res
print(send)
# iotqq_send(2,173225643,send)
iotqq_send(1, 2734184475, send)
email_send("2734184475@qq.com", send)

GetList(1)
user_IdStart = receive["id"]  # 获取程序开始运行时的第一id
# print(user_IdStart)
while True:
    GetList(1)  # 获取原始json数据 并检查cookie
    GetLogin()  # 获取个人信息
    # receive=receive_all+unFinish_all

    user_IdGet = receive["id"]  # 获取第一个人的姓名
    if user_IdGet == user_IdStart:  # 与开始的第一个人做比对,如果不一样就更新了
        time3 = datetime.datetime.now()
        CheckTime = time3.strftime('%Y-%m-%d %H:%M:%S')
        print("当前无更新惹~ 时间:" + CheckTime)
    else:
        time1 = datetime.datetime.now()
        CheckTime = time1.strftime('%Y-%m-%d %H:%M:%S')
        print("当前更新啦 时间:" + CheckTime)
        user_IdStart = user_IdGet  # 更新后把获取到的值传入初始值

        uers = GetOne(1)
        ret = HwkResult()
        res = user_all + "\n" + ret + "\n------------------------\n"

        send = "数据有更新啦!\n" + receiveX + "\n---更----新----数----据------\n" + res
        print(send)
        iotqq_send(1, 2734184475, send)
        iotqq_send(2, 173225643, send)
        email_send("2734184475@qq.com", send)
    time.sleep(10)
