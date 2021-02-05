# -*- coding: utf-8 -*-
'''
Author: whalefall
Date: 2021-02-05 09:57:03
LastEditors: whalefall
LastEditTime: 2021-02-05 10:25:41
Description: 生成并测试指定的ip段
'''

from IPy import IP
import re
import os
import sys
import time
import requests


def IPSplitStar(ips):  # 192.168.1.*  --->   192.168.1.1   到    192.168.1.255
    ip_1 = ips.split('.')[-4]
    ip_2 = ips.split('.')[-3]
    ip_3 = ips.split('.')[-2]
    ip_4 = ips.split('.')[-1]
    ip_to = []
    for i in range(1, 256):
        ip_result = ip_1 + '.' + ip_2 + '.' + ip_3 + '.' + str(i)
        ip_to.append(ip_result)
    return ip_to


def IPSplit_Star(ips):  # 192.168.1-10.*
    ip_1 = ips.split('-')[-2].split('.')[-3]
    ip_2 = ips.split('-')[-2].split('.')[-2]
    ip_3 = ips.split('-')[-2].split('.')[-1]  # 1
    ip_last = ips.split('-')[-1]  # 10
    ip_last_1 = ip_last.split('.')[-2]
    ip_3p = []
    for i in range(int(ip_3), int(ip_last_1)+1):
        for j in range(1, 256):
            ip_3p.append(ip_1 + '.' + ip_2 + '.' + str(i) + '.' + str(j))
    return ip_3p


def IPSplit(ip2ip_str):
    dic = []
    dic1 = []
    # filename = 'IP-range.txt'       #IP segment filename to be processed
    #fo = open(filename,"r")
    for line in ip2ip_str:  # for line in fo:
        data = line
        # Select the network segment type
        ips = re.search(
            r'((2[0-4]\d|25[0-5]|[01]{0,1}\d{0,1}\d)\.){3}(2[0-4]\d|25[0-5]|[01]{0,1}\d{0,1}\d)[-/]', line)
        if(ips != None):
            # Separate/type and -type
            ips = re.search(
                r'((2[0-4]\d|25[0-5]|[01]{0,1}\d{0,1}\d)\.){3}(2[0-4]\d|25[0-5]|[01]{0,1}\d{0,1}\d)[/]', line)

            # Processing/type
            if(ips != None):
                ip = IP(data)
                for x in ip:
                    dic.append(str(x))

            # process-type
            else:
                ip_1 = line.split('-')[-2].split('.')[-4]
                ip_2 = line.split('-')[-2].split('.')[-3]
                ip_3 = line.split('-')[-2].split('.')[-2]
                ip_4 = line.split('-')[-2].split('.')[-1]
                ip_last = line.split('-')[-1]
                ip_last.strip()
                ip_len = int(ip_last) - int(ip_4) + 1
                for i in range(ip_len):

                    ip_last = int(ip_4) + i
                    ip_result = ip_1 + '.' + ip_2 + \
                        '.' + ip_3 + '.' + str(ip_last)
                    dic.append(ip_result)
        else:
            # dic.append(data)
            if '*' in line and '-' in line:
                dic = dic + IPSplit_Star(line)
            elif '*' in line:
                dic = dic + IPSplitStar(line)
            else:
                dic.append(line)
    # print '查看结果  开始'
    # print dic
    # print '查看结果  结束'
    return list(set(dic))  # 目的是为了去重


def check_http(ip):
    resp = requests.get("http://{}".format(ip), timeout=2)
    if str(resp.status_code)=="200":
        with open("http200.txt","a") as f:
            f.write(ip+"\n")
            print("[Suc]{}".format(ip))
    else:
        print("[ERROR]{}".format(ip))
        

if __name__ == '__main__':
    # 203.195.64.0 203.195.95.255
    dic = IPSplit(['203.195.64-24.*', '203.195.95-255.*'])
    # dic = IPSplit(['192.168.1.1'])
    print(dic)
    for ip in dic:
        try:
            check_http(ip)
        except Exception as e:
            print("[Error]请求失败{}".format(ip))

    # print (len(dic))
    # print IPSplitStar('192.168.3.*')
    # print IPSplit_Star('192.168.1-2.*') #192.168.1-10.*  :
