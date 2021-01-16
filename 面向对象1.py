# 对象名开头大写
class Dog(object):

    typee = "宠物"  # 类变量

    # 初始化方法
    def __init__(self, name, age, color):  # self(我自己) 表示当前对象
        self.name = name  # 实例变量(属性)
        self.age = age
        self.color = color

    # 普通方法
    def eat(self, thing):
        print(self.name, "在啃", thing, "!")

    def run(self):
        print(self.name, "在跑")


# 实例化一个对象
dog = Dog("胡狗", 3, "灰色")  # 隐形传递self--dog
print(dog.self)
# dog.name="小可爱"
print(dog.name)

dog.eat("甜甜圈")  # 调用方法的对象是dog 故self也是dog
dog.run()


'''
对于以上我自己的理解如下： 
1. 创建了一个类，类名叫Dog. 
2. Dog下定义了三个函数分别为：__init__;eat;run 
3. __init__可以理解为双关语一
	可以理解为函数名为__init__;
	二可以理解吧init分开为in和it;
	在__init__函数里面（in）有一个它（it）;
	它又指向self;
4. self理解为 我自己定义;我自己定义了三个变量，名字叫name,age和color. 所以后面直接给变量赋值 
5. class Dog;def __init__;name  理解为大于或者高于后面一个等级 
6. dog=Dog() 理解为运行完函数后的结果赋值给变量dog dog和Dog是同一个级别 
7. dog.color 理解为调用Dog里面的color属性 开心
'''
