import requests

# 请求头
header = {
    "User-Agent": "Mozilla/5.0 (Linux;\
	Android 8.0; Pixel 2 Build/OPD3.17\
	0816.012) AppleWebKit/537.36 (KHTML,like\
	Gecko) Chrome/69.0.3497.100 Mobi \
	le Safari/537.36"
}

# 构造登录需要的参数
data = {
    "username": "2734184475@qq.com",
    "password": "xzwal123456"
}

# 创建session对象 不会像cookie那样会过期
ses = requests.session()

# 通过传递用户名密码得到cookie
ses.post(r"https://www.61host.cn/dologin.php", data=data)

# 请求需要的页面(登录后)
resp = ses.get("https://www.61host.cn/clientarea.php")

print(resp.content.decode())
