# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import DongguanItem
import re

class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        # 取出每个页面里帖子链接列表
        links = response.xpath("//div[@class='greyframe']/table//td/a[@class='news14']/@href").extract()
        # 迭代发送每个帖子的请求，调用parse_item方法处理
        for link in links:
            yield scrapy.Request(link, callback = self.parse_item)
        # 设置页码终止条件，并且每次发送新的页面请求调用parse方法处理
        if self.offset <= 150:
            self.offset += 30
            yield scrapy.Request(self.url + str(self.offset), callback = self.parse)

    # 处理每个帖子里
    def parse_item(self, response):
        item = DongguanItem()
        # 标题
        item['title'] = response.xpath('//span[@class="niae2_top"]/text()').extract()[0]

        #正文
        item['content'] = "".join(response.xpath('//td[@class="txt16_3"]/text()').extract())

        # 链接
        item['url'] = response.url

        yield item
        