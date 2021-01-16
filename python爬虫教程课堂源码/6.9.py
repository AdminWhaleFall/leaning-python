from aip import AipOcr
import re

APP_ID = '15469265'
API_KEY = 'rAGFtOChXtO7mnRPiwXg1Frf'
SECRET_KEY = 'Ailvoijh4X7lQIAoZ58UsGPlaDCmLIt7'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content(r'C:\Users\Administrator\Desktop\img\ee.jpg')

""" 调用通用文字识别, 图片参数为本地图片 """
data=str(client.basicGeneral(image)).replace(' ','')

pat=re.compile(r"{'words':'(.*?)'}")

result=pat.findall(data)[0]

print(result)