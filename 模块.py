# python中模块的目录
# C:\Users\27341\AppData\Local\Programs\Python\Python37-32\Lib
# 在安装目录的lib文件夹中
# 模块就是很多方法的集合
import random #导入随机数模块
a=random.random() #生成0-1的随机数 使用random模块下的random方法
print(a)
list=["花子君","嘤嘤","八寻宁宁"]
b=random.choice(list) #在列表中随机选择 使用random模块下的choice方法
print(b)
# 从random模块里边只引入choise方法 可以用 , 引入多个方法
from random import choice,random
from random import * #引入所有方法
#用from 下面调用方法时可以不用 random.choice 只用choice就可
print(choice([1,2,3]))
#生成1-10的随机整数
print(randint(1,10))
# 也可调用自己写的.py中的方法
import model
model.summ(23)
from model import summ
summ(100)

