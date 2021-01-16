# -*- coding: utf-8 -*-
import scrapy
import re
from mspider.items import MspiderItem
from mspider.items import TencentItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import random


class youdaoSpider(scrapy.Spider):
    # start_urls = ["http://www.example.com/"]
    name="youdao"
    allowed_domains = ["fanyi.youdao.com"]

    def start_requests(self):
        url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

        UserAgents=[
        "Mozilla/5.0 (Linux; U; An\
        droid 8.1.0; zh-cn; BLA-AL00 Build/HUAW\
        EIBLA-AL00) AppleWebKit/537.36 (KHTML, l\
        ike Gecko) Version/4.0 Chrome/57.0.2987.13\
        2 MQQBrowser/8.9 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; U; An\
        droid 8.1.0; zh-cn; BLA-AL00 Build/HUAW\
        EIBLA-AL00) AppleWebKit/537.36 (KHTML, l\
        ike Gecko) Version/4.0 Chrome/57.0.2987.13\
        2 MQQBrowser/8.9 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; U; An\
        droid 8.1.0; zh-cn; BLA-AL00 Build/HUAW\
        EIBLA-AL00) AppleWebKit/537.36 (KHTML, l\
        ike Gecko) Version/4.0 Chrome/57.0.2987.13\
        2 MQQBrowser/8.9 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; U; An\
        droid 8.1.0; zh-cn; BLA-AL00 Build/HUAW\
        EIBLA-AL00) AppleWebKit/537.36 (KHTML, l\
        ike Gecko) Version/4.0 Chrome/57.0.2987.13\
        2 MQQBrowser/8.9 Mobile Safari/537.36"
        ]

        UserAgent=random.choice(UserAgents)

        #构造请求头信息
        headers={
        "User-Agent":UserAgent

        }

        #向队列中加入一个带有表单信息的post请求
        yield scrapy.FormRequest(
            url=url,
            headers=headers,
            formdata={
                "i":"北京",
                "from":"AUTO",
                "to":"AUTO",
                "smartresult":"dict",
                "client":"fanyideskweb",
                "salt":"15503049709404",
                "sign":"3da914b136a37f75501f7f31b11e75fb",
                "ts":"1550304970940",
                "bv":"ab57a166e6a56368c9f95952de6192b5",
                "doctype":"json",
                "version":"2.1",
                "keyfrom":"fanyi.web",
                "action":"FY_BY_REALTIME",
                "typoResult":"false"
            },
            callback=self.parse
        )

    def parse(self, response):
        print("===========================")
        print(response.body)