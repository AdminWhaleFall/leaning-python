import re   # python 的正则库
import requests     # python 的requests库
import time

# #榜单第一页url
# http://www.htqyy.com/top/musicList/hot?pageIndex=0&pageSize=20
# #第二页
# http://www.htqyy.com/top/musicList/hot?pageIndex=1&pageSize=20
# #第三页
# http://www.htqyy.com/top/musicList/hot?pageIndex=2&pageSize=20

# #页码-1

# #歌曲url  http://www.htqyy.com/play/20

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

	idlist=re.findall(pat1,strr)
	titlelist=re.findall(pat2,strr)

	songID.extend(idlist)
	songName.extend(titlelist)


print(len(songID))
print(len(songName))






	


