import requests

#设置ip地址
proxy={
"http":"http://101.248.64.72:80",
"http":"http://101.248.64.68:80",
"https":"https://101.248.64.72:80",
}

response=requests.get("http://www.baidu.com",proxies=proxy)

print(response.content.decode())