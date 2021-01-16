#定义一个狗类
class Dog():
	typee="宠物狗" #属性（类变量）

	def __init__(self,a,b,c):#初始化方法 self当前对象
		self.name=a #属性（实例变量）
		self.age=b
		self.color=c

	def run(self):
		print("狗在飞快的跑！")
	def eat(self):
		print("狗在疯狂的啃骨头！")

# #实例化对象 自动调用了初始化方法
# dog=Dog("小黑",12,"白色")

# dog.color="黑色" #修改属性
# print(dog.color)#访问属性

# dog.run()#执行对象的方法



#定义一个狗类
class Cat():
	typee="宠物猫" #属性（类变量）

	def __init__(self,name):#初始化方法 self当前对象
		print("猫对象被创建啦！")
		self.name=name

	def run(self,speed):
		print(self.name,"在飞快的跑！速度：",speed)

	def eat(self):
		print("猫在疯狂的啃鱼！")

# cat=Cat("小喵")
# cat.run("30km/h")


class Employee():
	def __init__(self, empNum,name):
		self.empNum = empNum
		self.name = name

	def setnum(self,num):
		self.empNum=num

	def getnum(self):
		return self.empNum


emp=Employee("1001","zhangsan")
emp.setnum("1002")
num=emp.getnum()
print(num)


		

