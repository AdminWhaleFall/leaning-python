import scrapy
from mySpider.items import MusicItem
import re

class MusicSpider(scrapy.Spider):

	name = "music" #爬虫的识别名称，必须是唯一的，在不同的爬虫必须定义不同的名字

	allowed_domains = ["www.htqyy.com"] #域名范围，也就是爬虫的约束区域

	#爬取的URL元祖/列表
	start_urls = (
		'http://www.htqyy.com/top/musicList/hot?pageIndex=0&pageSize=20',
	)

	#解析的方法，每个初始URL完成下载后将被调用，
	#调用的时候传入从每一个URL传回的Response对象来作为唯一参数，主要作用如下：
	#负责解析返回的网页数据(response.body)，提取结构化数据(生成item)
	#生成需要下一页的URL请求。

	def parse(self, response):
		#filename = "music.html" #设定保存的文件
		#open(filename, 'wb').write(response.body)#保存到本地

		# 存放音乐信息集合
		#items = []

		titles=re.findall(r'target="play" title="(.*?)"',response.body.decode())
		artists=re.findall(r'target="_blank">(.*?)</a>',response.body.decode())

		for i in range(0,len(titles)):
			item=MusicItem()
			item['title']=titles[i]
			item['artist']=artists[i]

			#items.append(item)
			yield item #通过yield关键字的方式把每一个itme传到pipelines

		# 直接返回最后数据
		#print("=========",items)
		
		#return items



# json格式，默认为Unicode编码
# scrapy crawl music -o mu.json

# csv 逗号表达式，可用Excel打开
# scrapy crawl music -o mu.csv