'''
Author: WhaleFall
Date: 2021-01-28 11:10:10
LastEditTime: 2021-01-29 10:44:50
Description: 步步高家教机布丁乐园每日任务自动签到 收集东西
'''
import requests
requests.packages.urllib3.disable_warnings()
# 全局请求头
header = {
    "deviceModel": "S3 Pro",
    "apkVersionCode": "4060301",
    "vdeviceOSVersion": "V1.6.0_200516",
    "machineId": "70S3S8818DBCJ",
    "vapkPackageName": "com.bbk.personal",
    "token":
    "9aa7ea3400c7499e8cf562aa933059c59602dcfcde693e1017ad43d579916716dc6007f864e0faf0",
    "accountId": "25526831",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "276",
    "Host": "mark-incentive.eebbk.net",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.12.0"
}


def getTotalMark():
    # 查询金币数量
    url = "https://mark-incentive.eebbk.net/app/mark/getTotalMark"
    data = {
        "appKey": "申请的appkey",
        "apkVersionCode": 4060301,
        "apkPackageName": "com.bbk.personal",
        "deviceOSVersion": "V1.6.0_200516",
        "token":
        "9aa7ea3400c7499e8cf562aa933059c59602dcfcde693e1017ad43d579916716dc6007f864e0faf0",
        "accountId": 25526831,
        "deviceModel": "S3 Pro",
        "machineId": "70S3S8818DBCJ"
    }

    try:
        response = requests.post(url, headers=header, data=data,
                                 verify=False).json()
        if response["stateCode"] != "0":
            print("[Error]获取金币数量失败! 错误信息:{}".format(response["stateInfo"]))
        else:
            totalMark = response["data"]["totalMark"]
            print("[Sucess]获取成功!金币数量:{}".format(totalMark))

    except Exception as e:
        print("[Error]啊这! 请求发送未知错误 {}".format(str(e)))


# 查询任务列表
def getMarkDetail():
    data = {
        "appKey": 200,
        "apkVersionCode": 1000100,
        "apkPackageName": "com.eebbk.puddingmall",
        "deviceOSVersion": "V1.6.0_200516",
        "pi": 1,
        "token":
        "9aa7ea3400c7499e8cf562aa933059c59602dcfcde693e1017ad43d579916716dc6007f864e0faf0",
        "ps": 10,
        "accountId": 25526831,
        "endTime": -1,
        "startTime": -1,
        "deviceModel": "S3 Pro",
        "machineId": "70S3S8818DBCJ",
        "type": ""
    }
    url = "https://mark-incentive.eebbk.net/app/mark/getMarkDetail"
    response = requests.post(url, headers=header, data=data, verify=False)
    print(response.text)


# getMarkDetail()


# 完成任务
def completedTask():
    url = "https://mark-store.eebbk.net/mark-store/api/task/completedTask"
    headers = {
        "token":
        "9aa7ea3400c7499e8cf562aa933059c59602dcfcde693e1017ad43d579916716dc6007f864e0faf0",
        "machineId": "70S3S8818DBCJ",
        "accountId": "25526831",
        "apkPackageName": "com.eebbk.puddingmall",
        "apkVersionCode": "1000100",
        "deviceModel": "S3 Pro",
        "deviceOSVersion": "V1.6.0_200516",
        "Host": "mark-store.eebbk.net",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.12.0",
        "ruleCode": "300300302",
    }
    data = {
        "taskType": "2",
        "mark": "5",
        "appKey": "300",
        "ruleCode": "300300302",
        "moduleId": "300",
        "token":
        "9aa7ea3400c7499e8cf562aa933059c59602dcfcde693e1017ad43d579916716dc6007f864e0faf0",
        "accountId": 25526831,
        "taskName": "每日光顾",
        "taskId": 2,
        "machineId": "70S3S8818DBCJ",
    }
    response = requests.get(url, headers=headers, data=data, verify=False)
    print(response.text)


completedTask()