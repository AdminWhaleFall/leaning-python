import requests
import json

proxy={
"http":"http://113.120.39.37:9999",
"http":"http://113.120.39.37:9999",
}

#proxies 代理ip 多个时自动选择
resp=requests.get("http://pv.sohu.com/cityjson",proxies=proxy).text

#二进制再解码
print(resp)