from aip import AipOcr
import re
import requests

APP_ID="15725370"
API_KEY="t85bppstXXudNNSU0klALWgj"
SECRET_KEY="Zt7z61AXutINgWS1lqWe3xsWp9uePSFF"

client=AipOcr(APP_ID,API_KEY,SECRET_KEY)

data=requests.get(r"http://127.0.0.1:8020/登陆验证码/login.html").text

pat=re.compile(r'<img src="(.*?)" style')

url="http://127.0.0.1:8020/登陆验证码/"+pat.findall(data)[0]

image=requests.get(url).content


data=str(client.basicGeneral(image)).replace(" ","")

pat=re.compile(r"{'words':'(.*?)'}")

result=pat.findall(data)[0]

print(result)