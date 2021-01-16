# a=10000
# b=400

# 应纳税所得额=10000-400-5000=4600元

# 税=4600*0.1-210
import time


gongzi=float(input("请输入工资:"))
baoxian=float(input("请输入保险金额:"))

suode=gongzi-baoxian-5000
shui=0

if suode<=0:
	print("不用交税！")
else:
	if suode<3000:
		shui=suode*0.03-0
	elif suode<5000:
		shui=suode*0.1-210

print("您您需要交税：",shui,"到手工资：",gongzi-baoxian-shui)



time.sleep(60)