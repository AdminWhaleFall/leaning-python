import hashlib
import requests
import urllib.parse
import sys
import json
import re
import xlrd  # 读取Excel表格的库
import xlwt  # 写入Excel表格的库


def write_id(i):
    # 打开表格
    excel = xlrd.open_workbook(r"{}//初一学生期末成绩.xls".format(path))
    # 输出页签名
    # print(excel.sheet_names())
    # 打开页签
    sheet = excel.sheet_by_name("Sheet1")
    nrows = sheet.nrows  # 获取行数
    ncols = sheet.ncols  # 获取列数

    # 取出指定坐标里边的值(行数,列数) 坐标类似列表 从0开始的
    # i 取值1-nrows
    id = sheet.cell(i, 6).value.replace(" ", "").replace("\n", "").replace("\t", "")  # 身份证
    name = sheet.cell(i, 3).value.replace(" ", "").replace("\n", "").replace("\t", "")  # 姓名

    c = sheet.cell(i, 1).value  # 初二班级 初一班级直接加100得了
    numm = sheet.cell(i, 2).value  # 初二学号
    student = str(int(c) + 100) + str(int(numm))  # 拼接班级学号信息

    # 取出全部
    # for i in range(1, nrows):
    #     result = sheet.cell(i, 6).value.replace(" ", "").replace("/n", "")
    #
    #     print(result)

    return student, name, id

def md5(raw_txt):
    _md5_ = hashlib.md5()
    raw_txt = raw_txt.encode(encoding='utf-8')
    _md5_.update(raw_txt)
    return _md5_.hexdigest()


def login(pwd, name, schoolId, schoolName):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = "v=3.7&\
    osv=6.0.1&\
    deviceToken=E4%3AC4%3A83%3A2C%3A49%3A59&\
    driverType=OPPOA57&\
    client=student&\
    os=Android&driverCode=3.9.0&\
    pwd=" + str(pwd) + "&\
    schoolName=" + str(urllib.parse.quote(schoolName)) + "&\
    schoolId=" + schoolId + "&is_http=1&nicename=" + str(urllib.parse.quote(name))
    requests.packages.urllib3.disable_warnings()
    l = requests.post(url="https://mapi.ekwing.com/student/User/loginschool", data=data, headers=headers, verify=False)
    return l.text


def getList(tk, uid, _type):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = "v=3.7&\
        osv=6.0.1&deviceToken=E4%3AC4%3A83%3A2C%3A49%3A59&\
        driverType=OPPO%20A57&\
        client=student&os=Android&driverCode=3.9.0&\
        token=" + tk + "&\
        author_id=" + uid + "&\
        uid=" + uid + "&\
        type=" + _type + "&page=1&is_http=1"
    requests.packages.urllib3.disable_warnings()
    l = requests.post(url="https://mapi.ekwing.com/student/exam/getstuexamlist", data=data, headers=headers,
                      verify=False)
    return l.text


def getAreaList():
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = "v=3.7&\
        osv=6.0.1&\
        deviceToken=E4%3AC4%3A83%3A2C%3A49%3A59&\
        driverType=OPPO%20A57&\
        client=student&\
        os=Android&\
        driverCode=3.9.0&\
        is_http=1"
    requests.packages.urllib3.disable_warnings()
    l = requests.post(url="https://mapi.ekwing.com/student/user/getarealist", data=data, headers=headers, verify=False)
    return l.text


def getSchoolList(AreaId):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = "v=3.7&\
        osv=6.0.1&\
        deviceToken=E4%3AC4%3A83%3A2C%3A49%3A59&\
        driverType=OPPO%20A57&\
        client=student&\
        os=Android&\
        driverCode=3.9.0&\
        st_id=0&\
        id=" + AreaId + "&\
        is_http=1"
    requests.packages.urllib3.disable_warnings()
    l = requests.post(url="https://mapi.ekwing.com/student/user/scgetschool", data=data, headers=headers, verify=False)
    return l.text


################################################################################

raw_area = getAreaList()
L_schoolname = str()
L_shoolid = str()
area = json.loads(raw_area)
for province in area['data']:
    print(province['name'])
get_province = "广东"
for province in area['data']:
    if province['name'] == get_province:

        for city in province['city']:
            print(city['name'])
        get_city = "佛山"
        for city in province['city']:
            if city['name'] == get_city:

                for county in city['county']:
                    print(county['name'])
                get_county = "南海区"
                for county in city['county']:
                    if county['name'] == get_county:


                        raw_schools = getSchoolList(county['id'])
                        schools = json.loads(raw_schools)
                        for school in schools['data']:
                            print(school['name'])
                        get_school = "平洲第二初级中学"
                        for school in schools['data']:
                            if school['name'] == get_school:
                                print('选择成功！')
                                L_shoolid = school['id']
                                L_schoolname = school['name']

u_name = input("输入翼课网姓名:")
u_pwd = input("输入翼课网密码:")
dict_Elist = dict()
r_videos = str()
count = 0
i = str()
raw_results = login(md5(u_pwd), u_name, L_shoolid, L_schoolname)
if raw_results.find('error') != -1:
    print(":\\ Error:Wrong Password or User or School")
    input("PressEnterKeyToFuckingAway")
else:
    print("登录成功！")
    results = json.loads(raw_results)
    Token = results['data']['token']
    print("获取Token成功！")
    print(Token)
    Uid = results['data']['uid']
    raw_Elist = getList(Token, Uid, 'hold')
    Elist = json.loads(raw_Elist)
    for d in Elist['data']['list']:
        dict_Elist[d['self_title']] = d['self_id']

    print("获取作业列表成功！")
    print("未完成作业：")
    for title in dict_Elist.keys():
        print("名称：" + str(title) + "  id:" + str(dict_Elist[title]))

    raw_Elist = getList(Token, Uid, 'his')
    Elist = json.loads(raw_Elist)
    for d in Elist['data']['list']:
        dict_Elist[d['self_title']] = d['self_id']
    print("已完成作业：")
    for title in dict_Elist.keys():
        print("名称：" + str(title) + "  id:" + str(dict_Elist[title]))
    while 1:
        put = input("输入1获取听力原文+音频，输入2获取成绩，输入3直接完成作业，输入其他键退出：")
        if put == '1':

            get_ID = input("请输入需要获取听力原文+音频的作业id:")
            link = "https://mapi.ekwing.com/student/exam/basepage?uid=" + Uid + "&self_id=" + get_ID + "&product=student&os=Android&driverCode=3.9.0&v=3.7&token=" + Token + "&uid=" + Uid + "&is_http=1&author_id=" + Uid
            requests.packages.urllib3.disable_warnings()
            r_html = requests.get(link, verify=False)
            html = r_html.text
            pos = html.find("video_list: [")
            pos += 12
            while i != ']':
                i = html[pos]
                r_videos += i
                pos += 1
            r_videos = r_videos[1:-1]
            videos = re.split(',', r_videos)

            print("获取音频列表成功！\n准备下载...")
            print("任务：0/" + str(len(videos)))
            for work in videos:
                count += 1
                work = work.replace("\\", "", 9999)
                requests.packages.urllib3.disable_warnings()
                res = requests.get(work[1:-1], verify=False)
                with open(r"C:/Users/Public/Music/" + get_ID + '-' + str(count) + '.mp3', 'ab') as file:
                    file.write(res.content)
                    file.flush()
                print("已完成" + str(count) + '/' + str(len(videos)))
            print("已将音频下载到C:/Users/Public/Music \n准备获取听力原文...")

            raw_getTextJson = str()
            text_list = list()
            L_text = str()
            lis_text = list()
            raw_getTextJson = html
            F_text = re.search('"dis_text":"(.*?)",', raw_getTextJson)
            L_text = "原文：\n" + F_text.group(1) + "\n"
            lis_text = re.findall('"text":"(.*?)"', raw_getTextJson)
            for text in lis_text:
                L_text += str(text).replace(r"\n", " ") + "\n"
            lis_text = re.findall('"title_text":"(.*?)"', raw_getTextJson)
            for text in lis_text:
                L_text += str(text).replace(r"\n", " ") + "\n"
            print("听力原文提取成功！")
            with open(r"C:/Users/Public/Documents/" + get_ID + '-听力原文.txt', 'a') as file:
                file.write(L_text)
                file.flush()
            print("已将听力原文保存至C:/Users/Public/Documents/")
        elif put == '2':
            get_ID = input("请输入需要查询成绩的作业ID：")
            link = 'https://mapi.ekwing.com/student/exam/getscoreinfo?product=student&os=Android&driverCode=3.9.0&v=3.7&token=' + Token + '&uid=' + Uid + '&is_http=1&author_id=' + Uid + '&self_id=' + get_ID + '&method=exam_result&type=0'
            requests.packages.urllib3.disable_warnings()
            r_html = requests.get(link, verify=False)
            html = r_html.text
            score = re.search('"user_score":"(.*?)"', html)
            print("你的成绩是：" + str(score.group(1)))
        elif put == '3':
            get_ID = input("请输入需要直接完成的作业id:")
            link = "https://mapi.ekwing.com/student/exam/basepage?uid=" + Uid + "&self_id=" + get_ID + "&product=student&os=Android&driverCode=3.9.0&v=3.7&token=" + Token + "&uid=" + Uid + "&is_http=1&author_id=" + Uid
            requests.packages.urllib3.disable_warnings()
            r_html = requests.get(link, verify=False)
            html = r_html.text
            r_text = re.search('var tempDta = {(.*?)};', html)
            model_list = re.findall('"model_id":"(.*?)"', r_text.group(1))
            data = 'self_id=' + get_ID + '&answer_info=[{"model_id":"' + model_list[
                2] + '","model_type":"6","ques_list":[{"_from":"singsound","audioUrl":"https://m3.8js.net:99/20200306/70_zhifubaodaozhangshiwanyuan.mp3","details":[],"fluency":-1,"integrity":-1,"model_id":"' + \
                   model_list[
                       2] + '","offline":false,"pronunciation":-1,"recordId":"11eb04b9bc598124909ba10586513926","score":"100","model_type":"6","ques_id":-1}],"update_time":1601648140,"redotype":""}]&score_format=100&self_student_status=2&answer_time=100&uid=' + Uid + '&os=Android&driverCode=3.9.0&v=3.7&token=' + Token + '&is_http=1'

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
                       'Referer': 'https://mapi.ekwing.com/student/exam/loadexamtest?self_id=' + get_ID + '&self_mode_type=1&type=1&first=&uid=' + Uid + '&author_id=' + Uid + '&token=' + Token + '&v=3.7&is_http=1&os=Android&client=student&driverCode=3.9.0&product=student',
                       'Accept-Encoding': 'gzip, deflate, br',
                       'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'}
            requests.packages.urllib3.disable_warnings()
            l = requests.post(url='https://mapi.ekwing.com/student/exam/saveexamdraft', data=data, headers=headers,
                              verify=False)
            data = 'self_id=' + get_ID + '&answer_info=[{"model_id":"' + model_list[
                1] + '","model_type":"7","ques_list":[{"_from":"singsound","audioUrl":"https://m3.8js.net:99/20200306/70_zhifubaodaozhangshiwanyuan.mp3","details":[],"fluency":-1,"integrity":-1,"model_id":"824952","offline":false,"pronunciation":-1,"recordId":"11eb04b91d42a871872da10566516bb2","score":"100","model_type":"7","ques_id":"3"},{"_from":"singsound","audioUrl":"https://m3.8js.net:99/20200306/70_zhifubaodaozhangshiwanyuan.mp3","details":[],"fluency":-1,"integrity":-1,"model_id":"824952","offline":false,"pronunciation":-1,"recordId":"11eb04b92ae4e0b790c4a105665150d4","score":"100","model_type":"7","ques_id":"4"},{"_from":"singsound","audioUrl":"https://m3.8js.net:99/20200306/70_zhifubaodaozhangshiwanyuan.mp3","details":[],"fluency":-1,"integrity":-1,"model_id":"824952","offline":false,"pronunciation":-1,"recordId":"11eb04b938064e94a934a10566517d86","score":"100","model_type":"7","ques_id":"5"},{"_from":"singsound","audioUrl":"https://m3.8js.net:99/20200306/70_zhifubaodaozhangshiwanyuan.mp3","details":[],"fluency":-1,"integrity":-1,"model_id":"824952","offline":false,"pronunciation":-1,"recordId":"11eb04b9478d5a1ca53fa105665137a2","score":"100","model_type":"7","ques_id":"6"},{"_from":"singsound","audioUrl":"https://m3.8js.net:99/20200306/70_zhifubaodaozhangshiwanyuan.mp3","details":[],"fluency":-1,"integrity":-1,"model_id":"824952","offline":false,"pronunciation":-1,"recordId":"11eb04b955dcb55590fda1056651d4d8","score":"100","model_type":"7","ques_id":"7"},{"_from":"singsound","audioUrl":"https://m3.8js.net:99/20200306/70_zhifubaodaozhangshiwanyuan.mp3","details":[],"fluency":-1,"integrity":-1,"model_id":"824952","offline":false,"pronunciation":-1,"recordId":"11eb04b95ff517b9a61aa1056651f30e","score":"100","model_type":"7","ques_id":"8"}],"update_time":1601647981,"redotype":""}]&score_format=100&self_student_status=2&answer_time=143&uid=' + Uid + '&os=Android&driverCode=3.9.0&v=3.7&token=' + Token + '&is_http=1'
            requests.packages.urllib3.disable_warnings()
            l = requests.post(url='https://mapi.ekwing.com/student/exam/saveexamdraft', data=data, headers=headers,
                              verify=False)
            print(l.text)
            data = 'self_id=' + get_ID + '&answer_info=[{"model_id":"' + model_list[
                0] + '","model_type":"1","ques_list":[{"_from":"singsound","audioUrl":"https://m3.8js.net:99/20200306/70_zhifubaodaozhangshiwanyuan.mp3","details":[],"fluency":100,"integrity":100,"model_id":"824951","offline":false,"pronunciation":100,"recordId":"11eb04af6b462ef1b58fa105365100fc","score":"100","model_type":"1","ques_id":-1}],"update_time":1601643756,"redotype":""}]&score_format=100&self_student_status=2&answer_time=68&uid=' + Uid + '&os=Android&driverCode=3.9.0&v=3.7&token=' + Token + '&is_http=1'
            requests.packages.urllib3.disable_warnings()
            l = requests.post(url='https://mapi.ekwing.com/student/exam/saveexamdraft', data=data, headers=headers,
                              verify=False)
            print(l.text)
            data = 'self_id=' + get_ID + '&answer_time=900000&self_student_status=2&student_version=1&uid=' + Uid + '&os=Android&driverCode=3.9.0&v=3.7&token=' + Token + '&is_http=1'
            requests.packages.urllib3.disable_warnings()
            l = requests.post(url='https://mapi.ekwing.com/student/exam/submitexam', data=data, headers=headers,
                              verify=False)
            print(l.text)


        else:
            break

print("感谢使用 蓝鲸落-开发")
input(".")

##################################################################################
