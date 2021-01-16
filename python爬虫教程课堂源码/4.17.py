import urllib.request
import re

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/\
537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

url="https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20"

req=urllib.request.Request(url,headers=headers)

data=urllib.request.urlopen(req).read().decode()

pat1=r'"rating":\["(.*?)","\d+"\]'
pat2=r'"title":"(.*?)"'

pattern1=re.compile(pat1,re.I)
pattern2=re.compile(pat2,re.I)

data1=pattern1.findall(data)
data2=pattern2.findall(data)

print(data1,data2)

for x in range(len(data1)):
	print("排名：",x+1,"电影名：",data2[x],"豆瓣评分:",data1[x])




