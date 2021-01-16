#coding=utf-8
import requests
import re
import hashlib
import sys
import threading
lock=threading.Lock()
path=sys.path[0]

header={
	"User-Agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 5X Build/OPM1.171019.019; wv) \
	AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser\
	/6.2 TBS/045120 Mobile Safari/537.36 V1_AND_SQ_8.2.7_1334_YYB_D QQ/8.2.7.4410 NetType\
	/WIFI WebP/0.3.0 Pixel/1080 StatusBarHeight/72 SimpleUISwitch/0"
}

def getStrAsMD5(parmStr):
    #1、参数必须是utf8
    #2、python3所有字符都是unicode形式，已经不存在unicode关键字
    #3、python3 str 实质上就是unicode
    if isinstance(parmStr,str):
        # 如果是unicode先转utf-8
        parmStr=parmStr.encode("utf-8")
    m = hashlib.md5()
    m.update(parmStr)
    return m.hexdigest()

def getHead(qqID):

	global name
	url="https://users.qzone.qq.com/fcg-bin/cgi_get_portrait.fcg?uins="+str(qqID)
	resp=requests.get(url,headers=header).text
	# print(resp)
	#匹配头像地址
	pat_h=re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
	#匹配名字
	pat_n=re.compile('-1,0,0,0,"(.*?)",0]}')
	try:
		headURL=re.findall(pat_h,resp)[0]
		name=re.findall(pat_n,resp)[0]
	except:
		return "1"
	return headURL

def download(headURL):
	resp=requests.get(headURL,headers=header).content
	md5=getStrAsMD5(resp)
	# 空白头像 9e981dc7788599d9372c8381d776c554
	if md5=="9e981dc7788599d9372c8381d776c554":
		print("空白头像")
		pass
	else:
		img=requests.get(headURL,headers=header).content
		with open("{0}//img//{1}.jpg".format(path,str(qqID)+" "+name),"wb") as f:
			f.write(img)
		print(str(qqID)+" "+name,"已保存")

# qqID="2734184475"
# qqList=["2734184475"]

def run(thread):
	lock.acquire()
	for id in range(1000000000,9999999999):
		qqID=id
	
	url=getHead(qqID)
	if url=="1":
		print(thread,qqID,"用户不存在")
		pass
	else:
		with open("{0}//qqList.txt".format(path),"a",encoding="utf8") as l:
			l.write("qq号："+qqID+"  "+"网名："+name+"\n")
		download(url)
		print("-------------------------------")
	lock.release()



t1=threading.Thread(target=run,args=("线程1",))
t2=threading.Thread(target=run,args=("线程2",))
t3=threading.Thread(target=run,args=("线程3",))
	# if id%10=="2":
	# 	t2=threading.Thread(target=run,args=(id,"线程2",))
	# if id%10=="3":
	# 	t3=threading.Thread(target=run,args=(id,"线程3",))
	# if id%10=="4":
	# 	t4=threading.Thread(target=run,args=(id,"线程4",))
	# if id%10=="5":
	# 	t5=threading.Thread(target=run,args=(id,"线程5",))
	# if id%10=="6":
	# 	t6=threading.Thread(target=run,args=(id,"线程6",))
	# if id%10=="7":
	# 	t7=threading.Thread(target=run,args=(id,"线程7",))
	# if id%10=="8":
	# 	t8=threading.Thread(target=run,args=(id,"线程8",))
	# if id%10=="9":
	# 	t9=threading.Thread(target=run,args=(id,"线程9",))
	# if id%10=="0":
	# 	t10=threading.Thread(target=run,args=(id,"线程10",))

t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t6.start()
# t7.start()
# t8.start()
# t9.start()
# t10.start()






