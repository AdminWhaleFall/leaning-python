#2.15 实战：贴吧爬虫

from urllib import request
import urllib
import time

#构造请求头信息
header={
"User-Agent":"Mozilla/5.0 (Linux; U; An\
droid 8.1.0; zh-cn; BLA-AL00 Build/HUAW\
EIBLA-AL00) AppleWebKit/537.36 (KHTML, l\
ike Gecko) Version/4.0 Chrome/57.0.2987.13\
2 MQQBrowser/8.9 Mobile Safari/537.36"
}

#url规律

# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=0  #第一页 （1-1）*50

# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50 #第二页 （2-1）*50

# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100 #第三页 （3-1）*50

# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=150 #第四页（4-1）*50

# for i in range(1,4):
# 	print("http://tieba.baidu.com/f?kw=python&ie=utf-8&pn="+str((i-1)*50))

def loadpage(fullurl,filename):
	print("正在下载：",filename)
	req=request.Request(fullurl,headers=header)
	resp=request.urlopen(req).read()
	return resp


def writepage(html,filename):
	print("正在保存：",filename)

	with open(filename,"wb") as f:
		f.write(html)

	print("---------------------------")

#构造url
def tiebaSpider(url,begin,end):
	for page in range(begin,end+1):
		pn=(page-1)*50
		fullurl=url+"&pn="+str(pn) #每次请求的完整url
		filename="c:/第"+str(page)+"页.html" #每次请求后保存的文件名

		html=loadpage(fullurl,filename) #调用爬虫，爬取网页
		writepage(html,filename) #把获取到的网页信息写入本地

 


if __name__ == '__main__':

	kw=input("请输入贴吧名：")
	begin=int(input("请输入起始页："))
	end=int(input("请输入结束页："))

	url="http://tieba.baidu.com/f?"

	key=urllib.parse.urlencode({"kw":kw})

	url=url+key

	tiebaSpider(url,begin,end)

	time.sleep(10)




