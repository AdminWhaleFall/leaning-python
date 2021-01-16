#获取标签名和内容

from lxml import etree 

html = etree.parse("c:/file/hello.html")

#获取倒数第二个li元素下a的内容

#result1=html.xpath("//li[last()-1]/a")

# result2=html.xpath("//li/a")
# print(result1[-2].text) #.text获取标签内容


#获取 class 值为 bold 的标签名
result3=html.xpath("//*[@class='bold']")

print(result3[0].tag) #.tag表示获取标签名
