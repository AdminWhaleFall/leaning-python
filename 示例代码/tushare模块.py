# coding:utf-8
# get_realtime_quotes获取实时数据
# get_hist_data历史数据

import tushare
import pandas

class Share():
	"""docstring for ClassName"""
	def __init__(self):
		self.name = ""
		self.pb = 0
		self.code = "code"



# dataNow=tushare.get_realtime_quotes(code) #股票实时信息

# allData=tushare.get_hist_data(code)#股票历史信息

# sh=tushare.get_hist_data("sh")#指数历史信息

# chengjiao=tushare.get_today_ticks(code)#获取股票成交明细

# zhishu=tushare.get_index()#获取股票成交明细

df = tushare.get_sina_dd('002230', date='2018-10-16', vol=1000)#获取大单交易数据

print(df)

# news=tushare.get_latest_news()#获取最新财经新闻

# notice=tushare.get_notices("600106") #获取信息地雷

# #获取所有股票代码
# allShare=tushare.get_stock_basics()
#allCode=allShare.index.tolist() 

# print("股票实时信息===")
# print(dataNow)
# print("股票历史信息===")
# print(allData.iloc[1])
# print("上证指数===")
# print(sh.iloc[0])
# print(chengjiao)
# print(zhishu)

#print(news["title"])
# list1=allShare.index.tolist()

# list2=[]

# for x in range(len(list1)):
# 	ss=Share()
# 	ss.code=list1[x]
# 	ss.name=allShare["name"][x]
# 	ss.pb=allShare["pb"][x]
# 	list2.append(ss)



# list2=sorted(list2, key=lambda ss:ss.pb)

# for sss in list2:
# 	if sss.pb>0 and sss.pb<2:

# 		print(sss.code,sss.name,sss.pb)