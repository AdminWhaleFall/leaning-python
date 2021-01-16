# -*- coding:utf-8 -*- #设置编码格式
from urllib import request
import urllib
import time

#构造请求头信息
header={
	"User-Agent":"Mozilla/5.0 (Linux;\
	Android 8.0; Pixel 2 Build/OPD3.17\
	0816.012) AppleWebKit/537.36 (KHTML,like\
	Gecko) Chrome/69.0.3497.100 Mobi \
	le Safari/537.36"
}

# url规律
# https://tieba.baidu.com/f?kw=acg&ie=utf-8&pn=0 #第一页 (1-1)*50
# https://tieba.baidu.com/f?kw=acg&ie=utf-8&pn=50 #第二页 (2-1)*50 
# https://tieba.baidu.com/f?kw=acg&ie=utf-8&pn=100  #第三页 (3-1)*50 
# https://tieba.baidu.com/f?kw=acg&ie=utf-8&pn=150 #第4页 (4-1)*50 

# for i in range(1,4):
# 	print("https://tieba.baidu.com/f?kw=acg&ie=utf-8&pn="+str((i-1)*50))

# 爬虫
def loadpage(fullurl,filename):
	print("正在下载:",filename)
	#构造请求对象
	req=request.Request(fullurl,headers=header)
	#请求
	resp=request.urlopen(req).read()
	return resp

#文件保存
def writepage(html,filename):
	print("正在保存:",filename)

	#把获取到的二进制信息写入路径里面
	with open(filename,"wb") as f:
		f.write(html)

	print("-------------------")


# 爬虫+文件保存
def tiebaSpider(bagin,end):
	for page in range(bagin,end+1):
 		pn=(page-1)*50
 		fullurl=url+"&pn="+str(pn) #每次请求完整的url

 		filename=r"E:\我的坚果云\Python 学习\tieba\第"+str(page)+"页.html" #每次请求保存的文件名

 		#调用爬虫爬取网页信息
 		html=loadpage(fullurl,filename)

 		# 把爬取到的网页信息写入本地
 		writepage(html,filename)


# 双击 .py 文件时执行的东西
if __name__ == '__main__':
	kw=input("请输入要爬取的贴吧名:")
	bagin=int(input("请输入起始页码:")) 
	end=int(input("请输入结束页:")) 

	url="https://tieba.baidu.com/f?"
	#中文二进制转码
	key=urllib.parse.urlencode({"kw":kw})
	url=url+key
	
	tiebaSpider(bagin,end)

	time.sleep(10)
