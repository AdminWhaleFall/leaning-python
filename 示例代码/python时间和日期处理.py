import tushare
import datetime

# #获取当前日期和时间
# now=datetime.datetime.now()
# print(now)

#获取一个指定的日期
# d=datetime.datetime(2016,2,29,5,23,12)
# print(d)

# #日期转字符串
# now=datetime.datetime.now()
# strnow=now.strftime("%Y----%m----%d %H:%M:%S")
# print(strnow)

# #字符串转日期
# s="2018-9-11 23:01:02"
# d = datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
# print(type(d))

#日期比较
# d=datetime.datetime(2017,2,3,5,23,4)
# e=datetime.datetime(2017,2,1,5,23,12)
# j=e-d
# print(j.seconds)

# #日期相减
# day=now-d
# print(day.days)#获取相减天数
# print(day.seconds)#获取相减秒数

# #某个日期向前向后推移
# now=datetime.datetime.now()
# #d2=now+datetime.timedelta(hours=10)
# d3=now-datetime.timedelta(seconds=3600)
# print(d3)

# #获取星期
# now=datetime.datetime.now()
# d4=now+datetime.timedelta(days=10)
# a=d4.strftime("%w") #方法1
# a=d.weekday()+1 #方法2
# print("十天前是星期",a)

# #获取输入时间范围里每一个日期
# starttime="2018-10-1"
# endtime="2018-11-1"
# startdate=datetime.datetime.strptime(starttime,'%Y-%m-%d') 
# enddate=datetime.datetime.strptime(endtime,'%Y-%m-%d')
# datelist=[]#用list装日期
# if startdate<enddate:
# 	print(startdate,enddate)
# 	n=0
# 	while 1==1:
# 		onedate=startdate+datetime.timedelta(days=n)
# 		print("----------",onedate)
# 		n=n+1
# 		if onedate==enddate:
# 			break
# 		else:
# 			datelist.append(onedate)


#了解日历（Calendar）模块，自行上网了解

#获取一段时间范围内的工作日，需要下载安装business_calendar模块
# from business_calendar import Calendar, MO, TU, WE, TH, FR

# startdate= datetime.datetime(2018,10,1)#要获取18年10月工作日
# enddate = datetime.datetime(2018,10,31)

# cal=Calendar() #获取日历对象

# #自定义日期，workdays代表工作星期，holidays指定节假日列表
# hol=['2018-10-1','2018-10-2','2018-10-3','2018-10-4','2018-10-5','2018-10-6','2018-10-7']
# cal2=Calendar(workdays=[MO,TU,WE,TH,FR], holidays=hol)


# # count=cal2.busdaycount(startdate, enddate)#获取工作日天数,这里只考虑周末
# # print(count)
# daylist=cal2.range(startdate, enddate)#获取工作日列表,这里只考虑周末
# for x in daylist:
# 	print(x)






