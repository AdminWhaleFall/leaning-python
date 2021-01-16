from bs4 import BeautifulSoup

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

#根据CSS样式表查找标签 se|le|ct(选择)

soup=BeautifulSoup(html,"lxml")

#在css中选择器有：类(class)选择器(.),id选择器,标签选择器

#通过标签名c查找获取标签 返回的是一个列表
data=soup.select("a")
#通过类名查找
data=soup.select(".sister")
#通过id寻找
data=soup.select("#link2")

# 组合查找:查找p标签里边id=link1的标签
data=soup.select("p #link1")

#通过其他属性查找
#查找href=的a标签
# data=soup.select("a[href='http://example.com/elsie']")



print(data)