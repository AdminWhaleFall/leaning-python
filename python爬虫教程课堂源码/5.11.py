#图片爬虫
import urllib
import urllib.request
from lxml import etree

class Spider(object):
    def __init__(self):
        self.tiebaName="java"
        self.beginPage=1
        self.endPage=3
        self.url="http://tieba.baidu.com/f?"
        self.ua_header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}

    #构造url
    def tiebaSpider(self):
        pass

    #爬取页面内容
    def loadPage(self,url):
        pass

    #爬取帖子详情页，获得图片的链接
    def loadImages(self,link):
        pass

    #通过图片所在链接，爬取图片并保存图片到本地：
    def writeImages(self,imagesLink):
        pass

