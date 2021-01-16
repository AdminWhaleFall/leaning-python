# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#管道，负责item的后期处理或保存
class MspiderPipeline(object):

	#return item 必须要有
	def process_item(self, item, spider):
		return item
