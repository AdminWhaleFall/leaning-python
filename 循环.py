# i赋值给0~100 没有100 第二个不计入原则
'''
for i in range(58,100,2):
	print("第",i+2,"次")
'''

#等差数列求和
'''
#先定义和
sum = 0
for a in range(1,101,1):
	sum = sum + a
	# print(a)
print("1-100的和",sum)
'''

#列表寻找最大数值
'''
lis = [212,1231,13332,89,2,212121,42566,363425,35,1252,5,25,5,5,2352,452]
# 定义个参数
lmax = 0
for b in range(0,len(lis)-1):
	print("进入判断",lmax)
	if lmax<=lis[b]:
		lmax = lis[b]
		print("已获取当前最大值!",lmax)
	else:
		print("else 当前的最大值:",lmax,"小于的数值:",lis[b])
		print()
print(lmax)
'''

#while循环 灵活一些的
'''
c = 0
while c<=100:
	print(c)
	if c==50:
		print("c等于50啦")
	c+=1
'''
# while 循环嵌套
'''
d = 1
summ = 0
while d<=10:
	print("第",d,"年到了....")
	j = 0
	while j<12:
		j = j+1
		summ = summ+0.1
		# round(要四舍五入的数,小数点后保留的位数)
		print("第",d,"年","第",j,"月付款","累计付款",round(summ,2))
	d = d+1
'''

# continue 和 break 
'''
d = 1
summ = 0
while d<=10:
	print("第",d,"年到了....")
	if d==5:
		print("第",d,"不用付款...")
		d = d+1 #要加上1 不然反复跳入if 造成死循环
		continue #直接结束本次循环 开始下一次
		# break #跳出整个循环
	j = 0
	while j<12:
		j = j+1
		if j==6:
			print("这第",j,"月是小可爱生日 不用付款")
			continue
		summ = summ+0.1
		# round(要四舍五入的数,小数点后保留的位数)
		print("第",d,"年","第",j,"月付款","累计付款",round(summ,2))
	d = d+1
'''
# 死循环 可用于不断运行程序
'''
# 导入时间模块
import time
i = 0
while 1==1:
	i+=1
	print(i)
	# 休息1s
	time.sleep(1)
'''

