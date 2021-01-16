from bs4 import BeautifulSoup
import urllib
import urllib.request


headers={"User-Agent":"Mozilla/5.0\
(Windows NT 6.1; WOW64) AppleWe\
bKit/537.36 (KHTML, like Gecko) \
Chrome/57.0.2987.98 Safari/537.\
36 LBBROWSER"}

for x in range(0,20):
	page=10*x
	start={"start":page}
	start=urllib.parse.urlencode(start)
	url="https://hr.tencent.com/position.php?&"+start+"#a"

	req=urllib.request.Request(url,headers=headers)
	data=urllib.request.urlopen(req).read().decode()

	soup=BeautifulSoup(data,"lxml")
	urllist=soup.select('td a[target="_blank"]')

	for x in urllist:
		myurl="https://hr.tencent.com/"+x.attrs["href"]
		req2=urllib.request.Request(myurl,headers=headers)
		data=urllib.request.urlopen(req2).read().decode()

		print(data)





		

