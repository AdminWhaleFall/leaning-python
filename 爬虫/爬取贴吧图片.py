'''
https://tieba.baidu.com/f?kw=jvav&pn=0
https://tieba.baidu.com/f?kw=jvav&pn=50
https://tieba.baidu.com/f?kw=jvav&pn=100


'''
import requests
import time
from lxml import etree
from fake_useragent import UserAgent

ua=UserAgent().random

header={
	"UserAgent":ua
}



