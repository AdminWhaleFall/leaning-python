def summ(x):
	summ=0
	if x<=0:
		summ="请输入大于0的数"
	for i in range(0,x):
		i=i+1
		summ=summ+i
	types = type(summ)
	if types==0:
		summ="未知错误"
	print("从1加到",x,"的和为:",summ)