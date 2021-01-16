import datetime

#获取当前日期
# now=datetime.datetime.now()
# print(now)

#获取一个指定的日期
# d=datetime.datetime(2019,10,1,12,23,40)
# print(d)

#日期转字符串
# now=datetime.datetime.now()
# d=now.strftime("%Y====%m=====%d %H:%M:%S")
# print(d)

#字符串转日期
s="2020-8-15 2:30:20"
d=datetime.datetime.strptime(s,"%Y-%m-%d %H:%M:%S")
print(type(d))
