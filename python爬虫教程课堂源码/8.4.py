import re
import requests
import pymysql

#建立数据库连接
db=pymysql.Connect(host="localhost",port=3306,user="test",passwd="123321",db="spider",charset="utf8")
cursor=db.cursor()


#爬取数据
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Ap\
pleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Sa\
fari/537.36"
}

response=requests.get("http://changyongdianhuahaoma.51240.com/",headers=headers).text


#处理数据
pat1=r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>(.*?)</td>[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?</tr>'
pat2=r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?<td>(.*?)</td>[\s\S]*?</tr>'

pattern1=re.compile(pat1)
pattern2=re.compile(pat2)

data1=pattern1.findall(response)
data2=pattern2.findall(response)

#清空数据库原来的内容
sqll="delete from tel"
cursor.execute(sqll)
db.commit()

resultlist=[]
for i in range(0,len(data1)):
	resultlist.append(data1[i]+data2[i])

	sql="insert into tel(name,phone) values('"+data1[i]+"','"+data2[i]+"')"
	cursor.execute(sql)

print(resultlist)

db.commit()
db.close()


