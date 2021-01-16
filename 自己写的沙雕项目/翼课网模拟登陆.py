import requests #爬虫模块
from fake_useragent import UserAgent #随机ua模块
import re
# from bs4 import BeautifulSoup
import time

ua=UserAgent().random
cookie="IS_SCHOOL_LOGIN=1; zg_did=%7B%22did%22%3A%20%221738f42230516f-0fb5fcdda7ceab-7d56670e-15f900-1738f4223061a0%22%7D; Hm_lvt_70b7d1f99329b1ded9b60564cd0c45f6=1595836282,1595838359,1595930912; _pk_ses.1.1d65=*; Hm_lvt_b4c8ad78a28febf2e2e8a8d38c14165f=1595836285,1595930914; qimo_seosource_5f0f07f0-f16d-11e8-8f8c-a91ca374c015=%E7%AB%99%E5%86%85; qimo_seokeywords_5f0f07f0-f16d-11e8-8f8c-a91ca374c015=; href=https%3A%2F%2Fwww.ekwing.com%2Flogin%2Fview%3Fhref%3Dhttps%253A%252F%252Fwww.ekwing.com%252FHome%252Findex; accessId=5f0f07f0-f16d-11e8-8f8c-a91ca374c015; EKWUID=fNjc3ODg2NiMjMTA3OTMwMDM5MCMjOTBjNzkwNTI3NzMzZTY1ODQyNzMxYmNlMzUzYmMxOGIjIzFkOTk4NTg0OTkxNjk2YWE4M2I2OTYyNDhiNzA3ZGMwIyMxNTk2MDE3MzQyIyMxIyMyIyNla3dfc3R1ZGVudA%3D%3Dc; uid=nk4%2BKhMYXrGjNiP8hnKR1aKpetMFtlNaTQiDip52duU%3D; _pk_id.1.1d65=e9ec584ca2083854.1595836285.2.1595930945.1595839460.; Hm_lpvt_b4c8ad78a28febf2e2e8a8d38c14165f=1595930945; Hm_lpvt_70b7d1f99329b1ded9b60564cd0c45f6=1595930945; pageViewNum=2; zg_373b07f02b874fcda2f678ece32d3cea=%7B%22sid%22%3A%201595930946854%2C%22updated%22%3A%201595930951140%2C%22info%22%3A%201595836343057%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22%E5%AD%A6%E7%94%9F%E7%AB%AF%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.ekwing.com%22%2C%22cuid%22%3A%20%226778866%22%7D"
url="https://www.ekwing.com/Home/index"

ua=UserAgent().random
#构造请求头
header={
	"UserAgent":ua,
	"Cookie":cookie,
	"Referer":"https://www.ekwing.com/",
	"Host":"www.ekwing.com",
}

try:
	resp=requests.get(url,headers=header)
	print("翼课网http状态码:",resp.status_code)
	pat_resp=resp.content.decode()
	pat_name=r'__USERNAME__:"(.*?)"'
	name=re.findall(pat_name,pat_resp)
	print("当前cookie登陆的用户:",name[0])
except Exception as e:
	print("翼课网小爬虫出现异常:",e)
	#time.sleep(0.01)



# if __name__ == '__main__':
# 	run()

