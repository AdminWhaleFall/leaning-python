import requests
from lxml import etree
from fake_useragent import UserAgent
import json

url = "https://www.tool77.com/video/analysis"

header={
"Accept":"application/json, text/javascript, */*; q=0.01",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"zh-CN,zh;q=0.9",
"Connection":"keep-alive",
"Content-Length":"44",
"Cookie":"UM_distinctid=172b239f1935da-00a930cf471239-376b4502-1fa400-172b239f1945e6; JSESSIONID=EE4FF89D8FF5BD735841F0B38D91B49B; CNZZDATA1278695708=1997140613-1592127475-%7C1597059599; follow_wenkutool__keeper=oPEWiwfxCJ55PvZrBUiIhcObg2JA@@xSTe126",
"Host":"www.tool77.com",
"Origin":"https://www.tool77.com",
"Referer":"https://www.tool77.com/video",
"Sec-Fetch-Mode":"cors",
"Sec-Fetch-Site":"same-origin",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",

}


datafrom=json.dumps({
    "text":"https%3A%2F%2Fv.douyin.com%2FJ6bEtjg%2F"
})

resp=requests.post(url,data=datafrom,headers=header)
print(resp)




