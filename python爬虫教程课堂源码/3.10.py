import re   # python 的正则库
import requests     # python 的requests库
import time


# page=int(input("请输入您要爬取的页数："))

songID=[]
songName=[]

for i in range(0,2):
	url="http://www.htqyy.com/top/musicList/hot?pageIndex="+str(i)+"&pageSize=20"

	#获取音乐榜单的网页信息
	html=requests.get(url)

	strr=html.text

	pat1=r'title="(.*?)" sid'
	pat2=r'sid="(.*?)"'

	idlist=re.findall(pat2,strr)
	titlelist=re.findall(pat1,strr)

	songID.extend(idlist)
	songName.extend(titlelist)


for i in range(0,len(songID)):
	songurl="http://f2.htqyy.com/play7/"+str(songID[i])+"/mp3/2"
	songname=songName[i]

	data=requests.get(songurl).content

	print("正在下载第",i+1,"首")

	with open("E:\\music\\{}.mp3".format(songname),"wb") as f:
		f.write(data)

	time.sleep(0.5)






	


