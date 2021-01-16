import requests


id="6855637723840138504"
url="https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids="+id

header={
"UserAgent":"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac\
 OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version\
/5.0.2 Mobile/8J2 Safari/6533.18.5",
}

resp=requests.get(url,headers=header).json()


url_wm=resp["item_list"][0]["video"]["play_addr"]["url_list"][0].replace('playwm','play')
print(url_wm)

s=requests.session()

re=s.get(url=url_wm,headers=header)
url_real=re.url
print(url_real)

header1={
	"User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.20 SP-engine/2.16.0 baiduboxapp/11.20.0.14 (Baidu; P1 8.0.0)",
}

video=s.get(url=url_real,headers=header1)
print(video.url)

# with open(r"C:\Users\27341\Desktop\1.mp4","wb") as f:
# 	f.write(video.content)








