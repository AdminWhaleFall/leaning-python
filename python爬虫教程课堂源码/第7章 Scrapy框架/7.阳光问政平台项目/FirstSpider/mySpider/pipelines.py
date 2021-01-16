# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class MyspiderPipeline(object):

    def __init__(self):
        self.filename = open(r'sun.txt','a',encoding='utf-8')
        
    def process_item(self, item, spider):
        content = str(item)+ "\n"
        self.filename.write(content)
        return item

    def spider_closed(self, spider):
        self.filename.close()