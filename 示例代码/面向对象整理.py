#所有概念：类 对象 
#封装 继承 多态 
#属性 方法 
#构造方法 析构方法
#类变量（类属性） 实例变量（对象属性）
#私有方法 普通方法 类方法 静态方法 抽象方法
#抽象类（接口类）



#1.定义
# class Dog():
# 	type="宠物"  #类的属性
# 	def __init__(self, name,age):#初始化方法
# 		self.name = name         #对象属性
# 		self.age = age
# 	def eat(self):               #普通方法
# 		print(self.name,"在吃！")#self表示当前对象
# 	def run(self,speed):         #speed外部参数
# 		print("狗在跑！速度：",speed)

# dog=Dog("小黑",2) #实例化对象
# print(dog.name)   #获取对象属性
# dog.name="小白"   #更改对象属性
# dog.eat()         #调用方法，这时self会自动隐式传递进去
# dog.run(12)       #调用方法，传递外部参数进去
# 如果类属性和对象属性重名，优先使用对象属性。
# 如果用实例修改类变量，会给当前实例增加一个新的属性，
# 而不会真改变类变量，如果用类修改类变量，才会真正修改。


# 经典类和新式类
class A: #经典类
    pass

class B(object):#新式类
    pass


		

	













#2.析构函数
#class Dog():
# 	def __init__(self):#构造方法
# 		pass
# 	def __del__(self):               
# 		print("对象被销毁啦！")
# 	def run(self,speed):         
# 		pass
# 		
#dog=Dog()
#del dog #主动销毁对象







#3.私有属性和私有方法（封装）
# class Dog():
# 	def __init__(self, name,age):
# 		self.__name = name   #私有属性,只能类的内部能用
# 		self.age = age
# 	def __eat(self):         #私有方法,只能类的内部能用
# 		print(self.name,"在吃！")

# dog=Dog("小黑",2) 
#print(dog.name)   #获取不到
#dog.eat()         #执行不了
#print(dog._Dog__name)   #这样竟然获取到了属性









#4.继承
class Animal(object):#默认所有类最终都继承自object类
	def __init__(self, color):
		self.color = color
	def eat(self):
		print("动物在吃！")

class Cat(Animal):
	pass
		
class Dog(Animal):#继承了Animal类

	def __init__(self, name,age,color): #重写父类的构造方法
		super(Dog,self).__init__(color) #调用父类构造方法1,多继承时默认调用第一个
		#Animal.__init__(self,color)     #调用父类构造方法2
		self.name = name         
		self.age = age
	def eat(self):        #重写父类的方法
		Animal.eat(self)  #设置先执行父类的方法，再执行自己的               
		print(self.name,"在吃！")
	def run(self,speed):         
		print("狗在跑！速度：",speed)

cat=Cat("黄") #Cat类自动拥有了父类方法和属性，当然也可以自定义
#如果子类方法和父类方法重名，优先调用子类方法
dog=Dog("小黑",2,"黑") 
dog.eat()   
 






#5.多继承
# class A():
# 	def __init__(self):
# 		print("A")
# class B(A):
# 	def __init__(self):
# 		print("B")
# class C(A):
# 	def __init__(self):
# 		print("C")

# class D(B,C):
# 	def __init__(self):
# 	print("D")

# d=D()
#如果两个父类都有init方法，如果继承了前面的init方法，
#后面的init方法就不执行了
#py3按照广度优先来继承：D--B--C--A
#py2经典类按照深度优先（D--B--A--C），新式类按照广度优先来继承


















#6.多态
# class Animal(): #python中多态属于鸭子类型，这个父类可以不要
# 	def __init__(self, name):
# 		self.name = name
# 	def eat(self):
# 		pass

# class Cat(Animal):
# 	def eat(self):        
# 		print(self.name,"在吃！")
		
# class Dog(Animal):
# 	def eat(self):           
# 		print(self.name,"在吃！")

# def aEat(obj):
# 	obj.eat()













#7.静态方法和类方法
#@staticmethod
#静态方法，通过类直接调用，不需要创建对象，不会隐式传递self
#
#@classmethod
# 类方法，方法中的self是类本身，调用方法时传的值也必须是类的公有属性，
# 就是说类方法只能操作类本身的公有字段。
# 通过类和对象都可以调用。调用时传类名进去。
# class Cat():

# 	name="小喵"

# 	@staticmethod#静态方法
# 	def eat():   #不用传self    
# 		print(Cat.name,"吃！")#需要用类名得到属性

# 	@classmethod#类方法
# 	def run(self): #这里的self绑定的是类，普通方法里绑定的是对象
# 		print(self.name,"跑！")

# Cat.eat() #类名调用静态方法
# cat=Cat()
# cat.run() #对象名调用类方法
# Cat.run() #类名调用类方法












#8.抽象类和抽象方法
#抽象类：它的特殊之处在于只能被继承，不能被实例化，
#且子类必须实现抽象方法
#抽象类加抽象方法就相当于实现了接口的功能
#Python本身不提供抽象类和接口机制，
#要想实现抽象类，可以借助abc模块。ABC是Abstract Base Class的缩写
#
# import abc

# class Animal(metaclass=abc.ABCMeta): #声明抽象类
# 	def __init__(self, color):
# 		self.color = color

# 	@abc.abstractmethod
# 	def eat(self):#子类必须定义此功能
# 		pass

# class Cat(Animal):
# 	#pass
# 	def eat(self): #这个方法必须定义 
# 		print(self.name,"在吃！")

# cat=Cat("h")
