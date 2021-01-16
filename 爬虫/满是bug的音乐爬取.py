import requests
import re
import time

#请求头
header={
	"Accept":"text/plain, */*; q=0.01",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9",
"Connection":"keep-alive",
"Host":"www.htqyy.com",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
"X-Requested-With":"XMLHttpRequest",
# 添加这个参数破解反爬虫 服务器检测来路不正确。在headers里面添加User-Agent的同时还要加上Referer来伪装
"Referer":"http://www.htqyy.com/"
}

# url分析 2020.7.26 爬的
#第一页 http://www.htqyy.com/top/musicList/hot?pageIndex=0&pageSize=20
#第二页 http://www.htqyy.com/top/musicList/hot?pageIndex=1&pageSize=20
#第三页 http://www.htqyy.com/top/musicList/hot?pageIndex=2&pageSize=20
# pageIndex=页面-1
# 歌曲url http://f2.htqyy.com/play8/329/mp3/7
# http://f2.htqyy.com/play8/歌曲ID/mp3/7

# page=input(str("请输入您要爬取的页数:"))
page=1

#创建歌曲id title列表
idlist=[]
titlelist=[]

#获取title和ID
for i in range(0,page):
	#print("-----------------")
	# print("第",i+1,"页信息")
	url="http://www.htqyy.com/top/musicList/hot?pageIndex="+str(i)+"&pageSize=20"
	# print(url)
	resp=requests.get(url,headers=header)
	# print(resp.text)

	#数据清洗
	pat_title=r'title="(.*?)" sid'
	pat_sid=r'" sid="(.*?)">'

	SongTitle=re.findall(pat_title,resp.text)
	# print(SongTitle) #输出列表格式
	SongId=re.findall(pat_sid,resp.text)
	# print(SongId) #输出列表格式
	
	#extend 用新列表扩展原来的列表 旧列表.extend(新列表)
	titlelist.extend(SongTitle)
	# print(idlist)
	idlist.extend(SongId)
	# print(titlelist)

# for循环遍历idlist
for e in range(0,len(idlist)):
	song_url="http://f2.htqyy.com/play8/"+idlist[e]+"/mp3/7"
	song_name=titlelist[e]

	song_doc=requests.get(song_url,headers=header).content

	print("正在下载第",i+1,"首歌","名称为",song_name)
	with open("F:\music\{}.mp3".format(song_name),"wb") as f:
		f.write(song_doc)






