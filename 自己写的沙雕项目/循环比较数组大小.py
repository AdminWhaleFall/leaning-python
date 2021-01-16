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
