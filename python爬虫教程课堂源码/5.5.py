#标签和属性


#获取指定属性的标签

from lxml import etree 

html = etree.parse("c:/file/hello.html")

# result1=html.xpath("//li[@class='item-88']")

result2=html.xpath("//li/a[@href='link2.html']")

print(result2)

