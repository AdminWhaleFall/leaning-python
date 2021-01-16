# 股票提醒系统 tushare:python财经数据接口包
import tushare
dataNow=tushare.get_realtime_quotes("000591")
# pandas 里面的数据类型 生成一个表格

# 数据解析
name=dataNow.loc[0][0]
price=dataNow.loc[0][3]
high=dataNow.loc[0][4]
low=dataNow.loc[0][5]
volumn=dataNow.loc[0][8]
amount=dataNow.loc[0][9]
openToday=dataNow.loc[0][1]
pre_close=dataNow.loc[0][2]
timee=dataNow.loc[0][30]

print(name)

print("股票名:",name,"当前价格:",price,"最高价:",
	high,"最低价:",low,"成交量:",volumn,"成交额:",
	amount,"开盘价:",openToday,"收盘价:",pre_close,
	"时间:",timee)




