#获取标签信息

from bs4 import BeautifulSoup

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

# #根据标签名获取标签信息 soup.标签名
# print(soup.title)

# #获取标签内容
# print(soup.title.string)

# #获取标签名
# print(soup.title.name)

# #获取标签内所有属性
# print(soup.p.attrs["name"])

#获取直接子标签，结果是一个列表
# print(soup.head.contents)

#获取直接子标签，结果是一个生成器
# for i in soup.head.children:
# 	print(i)


#获取所有子标签，结果是一个生成器
for i in soup.p.descendants:
	print(i)



