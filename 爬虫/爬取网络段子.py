import requests
from lxml import etree
from fake_useragent import UserAgent
# 随机UA
ua=UserAgent().random

url="https://www.qiushibaike.com"
#构造请求头
header={
	"UserAgent":ua,
	# 服务器反爬虫,需加上来路判定
	"Referer":"https://www.qiushibaike.com/"
}

resp=requests.get(url,headers=header).text
#转化为xpath可处理的数据类型
html=etree.HTML(resp)
# 获取div里面的所有class为recmd-content的a标签里边的href属性
result=html.xpath('//div//a[@class="recmd-content"]/@href')
# print(result)

#https://www.qiushibaike.com/article/123386567

for site in result:
	xurl="https://www.qiushibaike.com"+site
	resp2=requests.get(xurl).text
	html2=etree.HTML(resp2)
	result2=html2.xpath("//div[@class='content']")
	print(result2[0].text)





