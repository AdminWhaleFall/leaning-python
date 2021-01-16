import re
import requests
import random
from fake_useragent import UserAgent

#随机生成UA模块
ua=UserAgent().random
# print(ua)

#请求头
header={
	"User-Agent":ua
}

url=r"http://www.114best.com/tel/"

response=requests.get(url,headers=header).content.decode()
print(response)

# <tr><td><a href="/tel/110/">匪警</a></td><td>110</td></tr>
# <tr><td>[\s\S]*?</a></td><td>(.*?)</td></tr>
pat_name=re.compile(r"<tr>[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?<td>^\s+[^\s-]+\s+$</td>[\s\S]*?</tr>")

print(pat_name.findall(response))


 # <tr>[\s\S]*?<td>(.*?)</td>[\s\S]*?<td>(.*?)</td>[\s\S]*?</tr>


