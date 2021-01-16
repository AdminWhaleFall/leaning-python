#搜索文档树  find_all()

from bs4 import BeautifulSoup

import re

#CSS 选择器：BeautifulSoup4
#和lxml 一样，Beautiful Soup 也是一个HTML/XML的解析器
#主要的功能也是如何解析和提取 HTML/XML 数据。


#模块下载安装：pip install bs4

#基础例子
html = """
<html><head><title>The Dormouse's story</title><title>The Dormouse's story2</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# #解析字符串形式的html
soup=BeautifulSoup(html,"lxml")

#默认只获取第一个 获取整个a标签里边的内容
# print(soup.a)

#获取全部a标签
# 根据字符串查找所有的a标签 返回一个结果集(ResultSet)
#结果集里边装的是标签对象tag

data=soup.find_all("a")
print(data[0]) #可以用下标取整个a标签
print(data[0].string) #获取a标签里面的内容
#用for循环遍历获取
for x in data:
	print(x.string)

print("-----------------------------")

#根据正则表达式查找标签，匹配标签名
data2=soup.find_all(re.compile("^b"))

for i in data2:
	print(i)

print("-----------------------------")

#根据属性查找标签
data3=soup.find_all(id="link2")

for i in data3:
	print(i)

print("-----------------------------")

#根据标签内容获取标签内容
data4=soup.find_all(text="Lacie")
data5=soup.find_all(text=["Lacie","Tillie"])
#找到内容中所有含有Do的 可以匹配正则
data6=soup.find_all(text=re.compile("Do"))
print(data6)


