#解析字符串形式的HTML
import requests
from lxml import etree #树形结构

'''
resp=requests.get("http://www.baidu.com").content.decode()
# print(resp)

#etree.HTML() 将字符串转化为了特殊的html对象 (自动补全缺失部分)
html=etree.HTML(resp)

#将HTML对象转成字符串 (序列化) encoding设置编码方式
result=etree.tostring(html,encoding="utf-8").decode()
print(result)
'''

#解析本地html
#处理网页的方式:
#1. 在爬虫中数据获取和数据清洗一体化 ,HTML()
#2. 数据获取和清洗分开 parse() (读取本地的html文件)

# etree.parse() 获取本地html文档
html=etree.parse(r"C:\Users\27341\Desktop\hello.html")

#转化为字符串
# result=etree.tostring(html,encoding="utf-8").decode()

# xpath获取一类标签
result=html.xpath("//a") #获取所有a标签标签里边的内容
#返回的结果是一个列表 要.text转化为文本
# print(result[3].text)

#获取指定属性的标签里边的内容
html.xpath("//li[@class='item-88']")

# 获取所有li标签下的a标签(子标签) a标签限定条件
result=html.xpath("//li/a[@href='link2.html']")

# print(result[0].text)

#获取标签的属性
#获取所有li标签的class属性
result=html.xpath("//li/a/@href")
#不需要进行任何处理直接获取属性值,返回列表,不会去重
# print(result)
#可以用for循环遍历列表取出每一个网站,再用request访问

#获取子标签
#获取下一级子标签
result=html.xpath("//li/a")
#获取所有子标签
result1=html.xpath("//li//span")
# print(result[1].text)


#获取li标签下a标签里所有的class
result2=html.xpath("//li/a//@class")
# print(result2[0])

#获取标签内容和标签名
# 获取倒数第二个li元素下的a内容 last()倒数
result3=html.xpath("//li[last()-1]/a")
result3=html.xpath("//li/a")
print(result3[-2].text) #.text 获取标签内容

#获取 class 值为 bold 的标签名
#//*文档中的所有标签 条件class为bold
result4=html.xpath("//*[@class='bold']")
print(result4[0]) #.tag 获取标签名



