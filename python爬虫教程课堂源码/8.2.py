import re
import requests
import xlsxwriter

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Ap\
pleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Sa\
fari/537.36"
}

response=requests.get("http://changyongdianhuahaoma.51240.com/",headers=headers).text

pat1=r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>(.*?)</td>[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?</tr>'
pat2=r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?<td>(.*?)</td>[\s\S]*?</tr>'

pattern1=re.compile(pat1)
pattern2=re.compile(pat2)

data1=pattern1.findall(response)
data2=pattern2.findall(response)

resultlist=[]

#创建表格
workbook=xlsxwriter.Workbook("demo2.xlsx")
worksheet=workbook.add_worksheet()

for i in range(0,len(data1)):
	resultlist.append(data1[i]+data2[i])

	#写入数据
	worksheet.write("A"+str(i+1),data1[i])
	worksheet.write("B"+str(i+1),data2[i])

print(resultlist)

workbook.close()



