# 类的封装,私有属性 方法
class Card(object):

	def __init__(self,num,pwd,ban):
		self.num = num
		self.pwd = pwd
		self.__ban = ban #余钱 __私有属性(只能在类的内部被访问)

	def cun(self):
		print("存款！")

	def getBan(self,numm,pwdd):
		# 加一层安全验证叭
		if numm==self.num and pwdd==self.pwd:
			# 把数值返回出去的方法
			return self.__ban
		else:
			return "输入错误"
		

		
card = Card("1001","123456",1000)
# 随意读取修改 不安全
# 
# 运行对象里边的getban方法 接收返回的ban值,也可以加层if验证
print(card.getBan("1222","2121"))

# 可以绕开安全验证,直接拿到私有属性 方法
print(card._Card__ban)
