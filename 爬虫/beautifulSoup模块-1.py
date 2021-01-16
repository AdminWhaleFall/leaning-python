from bs4 import BeautifulSoup
import requests


html="""
<html><head><title>我爱你</title></head>
"""

#解析字符串形式的HTML 自动处理缺失语法
soup=BeautifulSoup(html,"lxml")

#解析本地的HTML文件
# soup2=BeautifulSoup(open("index.html"))

# pret|ti|fy 格式化/美化HTML输出
# print(soup.prettify())

html=requests.get("https://www.yingyutu.com/").content.decode()
# print(html)

#解析字符串形式的HTML 自动处理缺失语法
soup=BeautifulSoup(html,"lxml")
# pret|ti|fy 格式化/美化HTML输出
# print(soup.prettify())

#根据标签名获取标签信息 soup.标签名
# 用xpath生成的是一组对象
print(soup.title)

#获取标签内容
print(soup.title.string)

#获取标签名
print(soup.title.name)

#获取标签内所有属性 默认只获取第一个 获取的是字典形式
print(soup.a.attrs['href'])

#获取直接子标签,结果是一个列表 .contents
# print(soup.head.contents)

# 生成器 for循环遍历读取 .children
# print(soup.head.children)

# for i in soup.head.children:
# 	print(i)

#获取所有子标签 结果是生成器 des|cen|dants：后代
# print(soup.descendants)

#遍历打印文本
for i in soup.p.descendants:
	print(i)
