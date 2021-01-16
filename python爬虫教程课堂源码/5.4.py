#获取一类标签
from lxml import etree

html=etree.parse(r"C:\file\hello.html")

result=html.xpath("//a") #获取所有span标签的信息


print(result[0].text)

