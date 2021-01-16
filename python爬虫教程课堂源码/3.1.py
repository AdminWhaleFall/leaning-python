#requests模块
#使用pip工具下载安装
import requests

#response=requests.get("http://wwww.baidu.com").content.decode()

response=requests.request("get","http://wwww.baidu.com").content.decode()

print(response)
