import time
import random
stop=5
time1=0
templist=[]
while True:
	for i in range(1,stop+1):
		time1=time1+1
		fh1=open(r"/sys/class/thermal/thermal_zone0/temp","r")
		temp=fh1.read()
		temp=float(temp/1000)
		temp_real=round(temp,2)
		fh1.close()
		print("树莓派当前温度为:",temp_real)
		templist.append(temp_real)
		print(i)
		if i/5==0:
			continue
		time.sleep(2)
	summ=0
	print("-------------")
	for e in range(0,len(templist)-1):
		summ=templist[e]+summ
	level=float(summ/len(templist))
	print("第",time1,"次的平均温度为",level)
	print("-------------")	
		


