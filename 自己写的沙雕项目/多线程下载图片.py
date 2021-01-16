import requests
import re
import time
import threading

url=r"http://www.dmoe.cc/random.php?return=json"

#构造请求头信息
header={
	"User-Agent":"Mozilla/5.0 (Linux;\
	Android 8.0; Pixel 2 Build/OPD3.17\
	0816.012) AppleWebKit/537.36 (KHTML,like\
	Gecko) Chrome/69.0.3497.100 Mobi \
	le Safari/537.36"
}

# timee=int(input("请问你要下载几张小可爱的图片鸭？"))
time=5
lock=threading.Lock()
getTime=0
def getpic(timee,getTime):
	lock.acquire()
	for i in range(0,timee):
		print("--------------")
		print("运行第",i+1,"次")
		try:
			#调用json方法 自动解析成json-->字典
			resp=requests.get(url,headers=header).json()

			imgurl=resp['imgurl']

			print("正在下载第",i+1,"张图片,地址为:",imgurl)
			img=requests.get(imgurl,headers=header).content

			with open(r"F:\二次元图片\{}.jpg".format(i+1+getTime),"wb") as f:
				f.write(img)
				f.close()
			print("第",i+1,"张图片下载完成！")
			#time.sleep(2)
		except Exception as e:
			print("程序运行出错:",e)
	lock.release()

getTime=0
for r in range(5):
	t=threading.Thread(target=getpic,args=(5,r,))
	t.start()
	



