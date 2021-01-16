#解析本地html
#爬虫中网页处理方式：
#1，在爬虫中，数据获取和数据清洗一体，HTML()
#2、数据获取和数据清洗分开，parse()

from lxml import etree 

#获取本地html文档
html=etree.parse(r"C:\file\hello.html")

result=etree.tostring(html,encoding="utf-8").decode()

print(result)

