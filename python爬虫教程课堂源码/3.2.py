import requests

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Ap\
pleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Sa\
fari/537.36"
}

wd={"wd":"中国"}

response=requests.get("http://www.baidu.com/s?",params=wd,headers=headers)

data=response.text #返回一个字符串形式的数据

data2=response.content #返回一个二进制形式的数据

print(data2.decode())
