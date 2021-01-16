#伪装浏览器的爬虫
from urllib import request
import re
import random

urllist=[
r"https://gitbook.cn/gitchat/columns?page=1&searchKey=&tag=",
r"https://gitbook.cn/gitchat/columns?page=2&searchKey=&tag=",
r"https://gitbook.cn/gitchat/columns?page=3&searchKey=&tag=",
r"https://gitbook.cn/gitchat/columns?page=4&searchKey=&tag=",
]

agent1="Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"
agent2="Mozilla/5.0 (Linux; Android 8.1; EML-AL00 Build/HUAWEIEML-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.143 Crosswalk/24.53.595.0 XWEB/358 MMWEBSDK/23 Mobile Safari/537.36 MicroMessenger/6.7.2.1340(0x2607023A) NetType/4G Language/zh_CN"
agent3="Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.4.994 Mobile Safari/537.36"
agent4="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
agent5="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
list1=[agent1,agent2,agent3,agent4,agent5]

agent=random.choice(list1)

#构造请求头信息
header={
"User-Agent":agent,
"Cookie":"__guid=54589117.3355346342630053000.1545469390794.6116; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1545469392; _ga=GA1.2.525028080.1545469392; customerId=5c1dfddd1c648b470dce01bc; customerToken=7094f880-05c8-11e9-b37a-bbc022d7aefd; customerMail=; isLogin=yes; __utmz=54589117.1550903385.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=54589117.525028080.1545469392.1550986423.1551265116.3; _gid=GA1.2.1073060500.1552831283; aliyungf_tc=AQAAAD/RilUP4wcAn/Q5cZh/y5cvhjrW; connect.sid=s%3AdBSjH13Adl1RlFsC2zZlAxGDmFh2kF_F.Yf52AS5i06bgo8lsniQWt1F4NtgmI3rOrmjBIiLwR6Q; SERVER_ID=5aa5eb5e-f0eda04d; Hm_lvt_5667c6d502e51ebd8bd9e9be6790fb5d=1551698067,1551698230,1552831282,1552908428; monitor_count=29; Hm_lpvt_5667c6d502e51ebd8bd9e9be6790fb5d=1552909773"
}

titlelist=[]
jianjielist=[]
ulist=[]

for i in urllist:
	req=request.Request(i,headers=header)
	reponse1=request.urlopen(req).read().decode()
	data1=re.findall(r'"topicTotalNum":\d+,"title":"(.{0,50}?)","columnType":\d+,"authorId":',reponse1)
	#data2=re.findall(r'"columnList":.*?"_id":"(.*?)"',reponse1)
	data3=re.findall(r'"columnTopics":.*?([(0-9)(a-z)(A-Z)]{24}).*?,"status"',reponse1)

	print(data3)

