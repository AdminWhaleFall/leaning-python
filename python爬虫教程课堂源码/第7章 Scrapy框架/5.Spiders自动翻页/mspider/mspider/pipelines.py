# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#管道，负责item的后期处理或保存
class MspiderPipeline(object):

	#定义一些需要初始化的参数(可以省略)
	def __init__(self): 
		self.file=open("music.txt","a")

	#管道每次接收到item后执行的方法(必须实现)
	#return item 必须要有
	def process_item(self, item, spider):
		#print("-------------",item)
		content=str(item)+"\n"
		self.file.write(content) #写入数据到本地
		return item

	# #当爬取结束时执行的方法(可以省略)
	# def close_spider(self,spider):
	# 	self.spider.close()
