#CSS选择器  select()
#根据css样式表来查找标签
from bs4 import BeautifulSoup


#基础例子
html = """
<html><head><title>The Dormouse's story</title><title>The Dormouse's story2</title></head>
<body>
<p class="title" name="dromouse"><b  class="sister" >The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# #解析字符串形式的html
soup=BeautifulSoup(html,"lxml")

#CSS选择器类型：标签选择器、类选择器、id选择器

#通过标签名查找
# data=soup.select("a")

#通过类名查找
# data=soup.select(".sister")

#通过id查找
# data=soup.select("#link2")

#组合查找
# data=soup.select("p #link1")

#通过其他属性查找
data=soup.select('a[href="http://example.com/tillie"]')


print(data)
