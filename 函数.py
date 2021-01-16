import time
# 定义方法

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
	
a=1
while True:
	a=a+1
	f1(a)
	time.sleep(1)

# return 理解
'''
def add(x,y,z):
	s=x+y+z
	# 返回s这个参数
	return s

# 新建变量并传入
summ1=add(1,2,3)
print(summ1)
#也可以直接当变量来使用
print("本次加和为:",add(1,2,3))
'''
#传参的几种方式
#顺序传入
def show(name,age,sex,hobby="21"): #形参
	print("我叫",name,"年龄",age,"性别",sex,"兴趣爱好",hobby)

#顺序传入
show("hyy",18,"女","追番")  #实参
#关键词传入
show(hobby="追番",sex="女",age=18,name="hyy")
#默认参数 优先传入手动给的参数
# def show(name,age,sex,hobby="21")
# 不定长参数(*args)(*abc),不确定参数的个数,参数的数据类型是元组
def addd(*args):
	summ2=0
	for i in args: #遍历元组
		summ2=summ2+i
	return summ2 #返回变量

summ2=addd(13,213,31,49,23,62) #接受变量
print(summ2)

# Python 内置函数 请参考文档
a=15.3
b=3
c=a/b
print(c) #在进行浮点运算时,由于进行进制转换,会出现精度误差
print(round(c,2)) #四舍五入 保留几位小数











		