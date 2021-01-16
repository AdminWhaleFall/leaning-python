#使用session实现登陆

import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

#创建session对象
ses=requests.session()

#构造登陆需要的参数
data={"email":"3254272716@qq.com","password":"123321a"}

#通过传递用户名密码得到cookie信息
ses.post("http://www.renren.com/PLogin.do",data=data)

#请求需要的页面
response=ses.get("http://www.renren.com/880151247/profile")

print(response.text)