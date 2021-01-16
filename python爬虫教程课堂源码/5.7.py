#获取子标签

from lxml import etree 

html = etree.parse("c:/file/hello.html")

result1=html.xpath("//li/a") #获取下一级子标签
result2=html.xpath("//li//span") #获取所有符合条件子标签

#print(result2[1].text)

#获取li标签下a标签里所有的class

result3=html.xpath("//li/a//@class")

print(result3)