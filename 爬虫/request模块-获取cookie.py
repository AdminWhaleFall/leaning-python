import requests

response=requests.get("http://www.baidu.com")

# 1.获取返回的 cookiejar 对象
cookiejar=response.cookies

# 2.将cookie转化为字典形式
cookiedict=requests.utils.dict_from_cookiejar(cookiejar)

print(cookiedict)

