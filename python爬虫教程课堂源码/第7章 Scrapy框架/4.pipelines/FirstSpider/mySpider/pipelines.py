# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class MyspiderPipeline(object):

	#准备一些需要的初始化参数
    def __init__(self):
        self.file = open('music.txt','a',encoding='utf-8')


     # 这个方法必须实现，每个item pipeline组件都需要调用该方法，
     # 这个方法必须返回一个 Item 对象，被丢弃的item将不会被之后的pipeline组件所处理。
    def process_item(self, item, spider): 
        content = str(item)+"\n"
        self.file.write(content)
        return item

    # 可选实现，当spider被关闭时，这个方法被调用
    def close_spider(self, spider):
        self.file.close()