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
        for page in range(self.beginPage,self.endPage+1):
            pn=(page-1)*50
            wo={'pn':pn,'kw':self.tiebaName}
            word=urllib.parse.urlencode(wo)
            myurl=self.url+word
            self.loadPage(myurl)

    #爬取页面内容
    def loadPage(self,url):
        req=urllib.request.Request(url,headers=self.ua_header)
        data=urllib.request.urlopen(req).read()

        html=etree.HTML(data)
        links=html.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')

        for link in links:
            link="http://tieba.baidu.com"+link
            self.loadImages(link)
            

    #爬取帖子详情页，获得图片的链接
    def loadImages(self,link):
        req=urllib.request.Request(link,headers=self.ua_header)
        data=urllib.request.urlopen(req).read()
        html=etree.HTML(data)
        links=html.xpath('//img[@class="BDE_Image"]/@src')
        print(links)


    #通过图片所在链接，爬取图片并保存图片到本地：
    def writeImages(self,imagesLink):
        pass


if __name__ == '__main__':

    mySpider=Spider()

    mySpider.tiebaSpider()