# coding=utf-8
import threading
from lxml import etree
import random
import requests
from fake_useragent import UserAgent
import json


ips_buff=[]
ips=[]
ips_http=[]
ips_http_buff=[]
time_delay=0
Proxy_Class=''
		
def test_ip_s(proxie):
	url=''
	Https_proxie={'http':'http://'+proxie,'https':'https://'+proxie}
	header= {'User-Agent':str(UserAgent().random)}
	if Proxy_Class=='https':
		url='https://www.baidu.com/'
	elif Proxy_Class=='http':
		url='http://ifconfig.me/ip'
	
	try:
		req = requests.get(url,headers=header,proxies = Https_proxie,timeout=time_delay)
		if req.status_code == 200:
			if Proxy_Class=='https':
				ips.append(proxie)
			elif Proxy_Class=='http':
				ips_http.append(proxie)
	except:
		return False


#获取快代理	
def get_kuai(page):
	URL='https://www.kuaidaili.com/ops/proxylist/%s/'%page
	header= {'User-Agent':str(UserAgent().random)}
	try:
		kuai_res = requests.get(URL,headers=header,timeout=5)
		if(kuai_res.status_code	!=	200):
			return False
		html_ele=etree.HTML(kuai_res.content)
		tr_eles=html_ele.xpath('//*[@id="freelist"]/table/tbody/tr')
		for tr_ele in tr_eles:
			ip_str=tr_ele.xpath('./td[1]/text()')[0]
			port=tr_ele.xpath('./td[2]/text()')[0]
			http_str=tr_ele.xpath('./td[4]/text()')[0]
			if http_str =='HTTP, HTTPS':
				ips_buff.append(ip_str+':'+port)
			elif http_str =='HTTPS':
				ips_buff.append(ip_str+':'+port)
			else:
				ips_http_buff.append(ip_str+':'+port)
	except:
		# print("获取代理失败")
		return False

			
#获取西拉代理
def get_xila(page):
	URL='http://www.xiladaili.com/gaoni/%s'%page
	header= {'User-Agent':str(UserAgent().random)}
	try:
		xila_res = requests.get(URL,headers=header,timeout=5)
		if(xila_res.status_code	!=	200):
			return False
		html_ele=etree.HTML(xila_res.content)
		tr_eles=html_ele.xpath('/html/body/div/div[3]/div[2]/table/tbody/tr')
		for tr_ele in tr_eles:
			ip_port_str=tr_ele.xpath('./td[1]/text()')[0]
			http_str=tr_ele.xpath('./td[2]/text()')[0]
			if http_str =='HTTP,HTTPS代理':
				ips_buff.append(ip_port_str)
			elif http_str =='HTTPS代理':
				ips_buff.append(ip_port_str)
			else:
				ips_http_buff.append(ip_port_str)
	except:
		# print("获取代理失败")
		return False
		
def get_xila_https(page):
	URL='http://www.xiladaili.com/https/%s/'%page
	header= {'User-Agent':str(UserAgent().random)}
	try:
		xila_res = requests.get(URL,headers=header,timeout=5)
		if(xila_res.status_code	!=	200):
			return False
		html_ele=etree.HTML(xila_res.content)
		tr_eles=html_ele.xpath('/html/body/div/div[3]/div[2]/table/tbody/tr')
		for tr_ele in tr_eles:
			ip_port_str=tr_ele.xpath('./td[1]/text()')[0]
			ips_buff.append(ip_port_str)
			
	except:
		# print("获取代理失败")
		return False

#获取西刺代理
def get_xici(page):
	header= {'User-Agent':str(UserAgent().random)}
	url = 'https://www.xicidaili.com/nn/%s'%page
	try:
		response = requests.get(url, headers=header,timeout=5)
		if(response.status_code != 200):
			return False
		html_ele = etree.HTML(response.content)
		tr_eles = html_ele.xpath('//table[@id="ip_list"]//tr')
		tr_eles.pop(0)
		for tr_ele in tr_eles:
			ip_str = tr_ele.xpath('./td[2]/text()')[0]
			port = tr_ele.xpath('./td[3]/text()')[0]
			http_str= tr_ele.xpath('./td[6]/text()')[0]
			if http_str=='HTTPS':
				ips_buff.append( ip_str + ':' + port)
			else:
				ips_http_buff.append(ip_str + ':' + port)
	except:
		# print("获取代理失败")
		return False
		
#获取IP3366代理		
def get_IP3366(page):
	URL='http://www.ip3366.net/?stype=1&page=%s'%page
	header= {'User-Agent':str(UserAgent().random)}
	try:
		IP3366_res = requests.get(URL,headers=header,timeout=5)
		if(IP3366_res.status_code	!=	200):
			return False
		html_ele=etree.HTML(IP3366_res.content)
		tr_eles=html_ele.xpath('//*[@id="list"]/table/tbody/tr')
		for tr_ele in tr_eles:
			ip_str=tr_ele.xpath('./td[1]/text()')[0]
			port=tr_ele.xpath('./td[2]/text()')[0]
			http_str=tr_ele.xpath('./td[4]/text()')[0]
			if http_str =='HTTPS':
				ips_buff.append(ip_str + ':' + port)
			else:
				ips_http_buff.append(ip_str + ':' + port)
	except:
		return False

#获取IP3366代理		
def get_7yip(page):
	URL='https://www.7yip.cn/free/?action=china&page=%s'%page
	header= {'User-Agent':str(UserAgent().random)}
	try:
		IP7y_res = requests.get(URL,headers=header,timeout=5)
		if(IP7y_res.status_code	!=	200):
			return False
		html_ele=etree.HTML(IP7y_res.content)
		tr_eles=html_ele.xpath('//*[@id="content"]/section/div[2]/table/tbody/tr')
		for tr_ele in tr_eles:
			ip_str=tr_ele.xpath('./td[1]/text()')[0]
			port=tr_ele.xpath('./td[2]/text()')[0]
			http_str=tr_ele.xpath('./td[4]/text()')[0]
			if http_str =='HTTPS':
				ips_buff.append(ip_str+':'+port)
			else:
				ips_http_buff.append(ip_str + ':' + port)
	except:
		return False

		
def get_freeIP(page):
	header= {'User-Agent':str(UserAgent().random)}
	url='https://www.freeip.top/?page=%s&protocol=https'%page
	
	try:
		response = requests.get(url, headers=header,timeout=5)
		if(response.status_code != 200):
			return False
		html_ele = etree.HTML(response.content)
		tr_eles = html_ele.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/table/tbody/tr')
		for tr_ele in tr_eles:
			ip_str = tr_ele.xpath('./td[1]/text()')[0]
			port = tr_ele.xpath('./td[2]/text()')[0]
			ips_buff.append( ip_str + ':' + port)
	except:
		# print("获取代理失败")
		return False
		
		
def get_nimaIP(page):
	header= {'User-Agent':str(UserAgent().random)}
	url='http://www.nimadaili.com/gaoni/%s/'%page
	
	try:
		response = requests.get(url, headers=header,timeout=5)
		if(response.status_code != 200):
			return False
		html_ele = etree.HTML(response.content)
		tr_eles = html_ele.xpath('/html/body/div/div[1]/div/table/tbody/tr')
		for tr_ele in tr_eles:
			ip_str_port = tr_ele.xpath('./td[1]/text()')[0]
			http_str = tr_ele.xpath('./td[2]/text()')[0]
			if http_str=='HTTP,HTTPS代理':
				ips_buff.append(ip_str_port)
			elif http_str=='HTTPS代理':
				ips_buff.append(ip_str_port)
			else:
				ips_http_buff.append(ip_str_port)
	except:
		# print("获取代理失败")
		return False
		
def get_nimahttps(page):
	header= {'User-Agent':str(UserAgent().random)}
	url='http://www.nimadaili.com/https/%s/'%page
	
	try:
		response = requests.get(url, headers=header,timeout=5)
		if(response.status_code != 200):
			return False
		html_ele = etree.HTML(response.content)
		tr_eles = html_ele.xpath('/html/body/div/div[1]/div/table/tbody/tr')
		for tr_ele in tr_eles:
			ip_str_port = tr_ele.xpath('./td[1]/text()')[0]
			ips_buff.append(ip_str_port)
	except:
		# print("获取代理失败")
		return False

def getProxy(page):
	if page == 1:
		proxy_url='https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list'
		header= {'User-Agent':str(UserAgent().random)}
		try:
			response = requests.get(proxy_url,headers=header,timeout=5)
			proxies_list = response.text.split('\n')
			for proxy_str in proxies_list:
				proxy_json = json.loads(proxy_str)
				host = proxy_json['host']
				port = proxy_json['port']
				type = proxy_json['type']
				if type =='https':
					ips_buff.append(host	+	':'	+	port)
				else:
					ips_http_buff.append(host	+	':'	+	port)
		except:
			return False
				
			
			
def verify1(statr,num):
	for n in range(statr,num):
		if Proxy_Class=='https':
			test_ip_s(ips_buff[n])
		elif Proxy_Class=='http':
			test_ip_s(ips_http_buff[n])
		print('线程1校验代理进度%.1f%%'%((n+1)*100/num))
		
def verify2(statr,num):
	for n in range(statr,num):
		if Proxy_Class=='https':
			test_ip_s(ips_buff[n])
		elif Proxy_Class=='http':
			test_ip_s(ips_http_buff[n])
		print('线程2校验代理进度%.1f%%'%((n+1-statr)*100/(num-statr)))
		
def verify3(statr,num):
	for n in range(statr,num):
		if Proxy_Class=='https':
			test_ip_s(ips_buff[n])
		elif Proxy_Class=='http':
			test_ip_s(ips_http_buff[n])
		print('线程3校验代理进度%.1f%%'%((n+1-statr)*100/(num-statr)))

def verify4(statr,num):
	for n in range(statr,num):
		if Proxy_Class=='https':
			test_ip_s(ips_buff[n])
		elif Proxy_Class=='http':
			test_ip_s(ips_http_buff[n])
		print('线程4校验代理进度%.1f%%'%((n+1-statr)*100/(num-statr)))

def verify5(statr,num):
	for n in range(statr,num):
		if Proxy_Class=='https':
			test_ip_s(ips_buff[n])
		elif Proxy_Class=='http':
			test_ip_s(ips_http_buff[n])
		print('线程5校验代理进度%.1f%%'%((n+1-statr)*100/(num-statr)))
		
def verify6(statr,num):
	for n in range(statr,num):
		if Proxy_Class=='https':
			test_ip_s(ips_buff[n])
		elif Proxy_Class=='http':
			test_ip_s(ips_http_buff[n])
		print('线程6校验代理进度%.1f%%'%((n+1-statr)*100/(num-statr)))
		
def verify7(statr,num):
	for n in range(statr,num):
		if Proxy_Class=='https':
			test_ip_s(ips_buff[n])
		elif Proxy_Class=='http':
			test_ip_s(ips_http_buff[n])
		print('线程7校验代理进度%.1f%%'%((n+1-statr)*100/(num-statr)))
		
def verify8(statr,num):
	for n in range(statr,num):
		if Proxy_Class=='https':
			test_ip_s(ips_buff[n])
		elif Proxy_Class=='http':
			test_ip_s(ips_http_buff[n])
		print('线程8校验代理进度%.1f%%'%((n+1-statr)*100/(num-statr)))

def verify9(statr,num):
	for n in range(statr,num):
		if Proxy_Class=='https':
			test_ip_s(ips_buff[n])
		elif Proxy_Class=='http':
			test_ip_s(ips_http_buff[n])
		print('线程9校验代理进度%.1f%%'%((n+1-statr)*100/(num-statr)))

def verify10(statr,num):
	for n in range(statr,num):
		if Proxy_Class=='https':
			test_ip_s(ips_buff[n])
		elif Proxy_Class=='http':
			test_ip_s(ips_http_buff[n])
		print('线程10校验代理进度%.1f%%'%((n+1-statr)*100/(num-statr)))




def get_proxy(Proxy_Type,timeout):
	global ips_buff
	global ips
	global time_delay
	global ips_http
	global ips_http_buff
	global Proxy_Class
	
	Proxy_Class=Proxy_Type
	time_delay=timeout
	verify_threads=[]
	n=0
	ips.clear()
	ips_buff.clear()
	ips_http.clear()
	ips_http_buff.clear()

	print('获取免费可用代理')
	for n in range(1,11):
		get_kuai(n)
		get_nimahttps(n)
		get_xila(n)
		get_xici(n)
		get_freeIP(n)
		get_7yip(n)
		get_IP3366(n)
		get_nimaIP(n)
		get_xila_https(n)
		getProxy(n)
		print('获取代理进度%d%%'%(n*10))
	
	if Proxy_Class=='https':
		ips_buff=list(set(ips_buff))
		print('HTTPS代理总数：%d'%len(ips_buff))
	elif Proxy_Class=='http':
		ips_http_buff=list(set(ips_http_buff))
		print('HTTP代理总数：%d'%len(ips_http_buff))
	
	print('')
	print('多线程校验代理......')
	print('')
	start1=0
	start2=0
	if Proxy_Class=='https':
		start1=int(len(ips_buff)/10)
		start2=len(ips_buff)
	elif Proxy_Class=='http':
		start1=int(len(ips_http_buff)/10)
		start2=len(ips_http_buff)

	if len(ips_buff)!=0 or len(ips_http_buff)!=0:
		t1 = threading.Thread(target=verify1,args=(0,start1))
		verify_threads.append(t1)
		t2 = threading.Thread(target=verify2,args=((start1+1),start1*2))
		verify_threads.append(t2)
		t3 = threading.Thread(target=verify3,args=((start1*2+1),start1*3))
		verify_threads.append(t3)
		t4 = threading.Thread(target=verify4,args=((start1*3+1),start1*4))
		verify_threads.append(t4)
		t5 = threading.Thread(target=verify5,args=((start1*4+1),start1*5))
		verify_threads.append(t5)
		t6 = threading.Thread(target=verify6,args=((start1*5+1),start1*6))
		verify_threads.append(t6)
		t7 = threading.Thread(target=verify7,args=((start1*6+1),start1*7))
		verify_threads.append(t7)
		t8 = threading.Thread(target=verify8,args=((start1*7+1),start1*8))
		verify_threads.append(t8)
		t9 = threading.Thread(target=verify9,args=((start1*8+1),start1*9))
		verify_threads.append(t9)
		t10 = threading.Thread(target=verify10,args=((start1*9+1),start2))
		verify_threads.append(t10)

		
		for t in verify_threads:	
			t.start()
		for t in verify_threads:
			t.join()

	print('校验代理完成')
	if len(ips)!=0 or len(ips_http_buff)!=0:
		if Proxy_Class=='https':
			return ips
		elif Proxy_Class=='http':
			return ips_http
	else:
		print('无可用代理，请稍后再试')
		return False

	
# def main():
	# get_proxy(0.2)

# if __name__=='__main__':
	# main()
	


