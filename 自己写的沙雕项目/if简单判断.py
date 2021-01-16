# # 简单if判断 
# a = 2
# if a>0: #被执行
# 	print("a大于0")
# if a<0: #被执行
# 	print("a小于0")
# else: #第二个if执行的结果
# 	print("其他")
# # elif多条件判断
# # 若前面的条件满足就不会再执行下去
# b = 2
# if b>0 and b<3:
# 	print("b大于0")
# elif b>3:
# 	print("b大于3")
# elif b<21:
# 	print("b小于21")
# 循环
# range 生成0-100的序列并循环赋值给i
for a in range(50,100,2): #对序列进行遍历
	print(a)
	print("")