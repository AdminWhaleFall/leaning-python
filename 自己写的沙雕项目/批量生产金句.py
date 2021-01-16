import requests
import re
import time

url="https://v1.hitokoto.cn"

while True:
	
	try:
		rep=requests.get(url).json()
		hitokoto=rep['hitokoto']
		print(hitokoto)
	except Exception as e:
		print("错误:",e)
	time.sleep(1)






