#爬取糗事百科段子
import requests
from lxml import etree 

url = 'https://www.qiushibaike.com/'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)\
	AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0\
	.2743.116 Safari/537.36',
	'Accept-Language': 'zh-CN,zh;q=0.8'}


response=requests.get(url,headers=headers).text

html=etree.HTML(response)

result1=html.xpath('//div//a[@class="recmd-content"]/@href')

#print(result1)

#https://www.qiushibaike.com/article/121207030

for site in result1:
	xurl="https://www.qiushibaike.com"+site
	response2=requests.get(xurl).text
	html2=etree.HTML(response2)
	result2=html2.xpath("//div[@class='content']")

	print(result2[0].text)