# 类的继承
# object是所有类的符类 Animal类继承object类
class Animal(object):

    # 初始化方法
    def __init__(self, color):
        self.color = color

    def eat(self):
        print("动物在吃东西")

    def run(self):
        print("动物在跑")

# Cat类继承Animal类


class Cat(Animal):

    def eat(self):
        print("小猫在吃鱼")


class Dog(Animal):

    def __init__(self, name, age, color):
        # 调用父类的初始化方法
        # super:父类方法 Dog:子类 定义初始化方法中的color参数
        super(Dog, self).__init__(color)
        self.name = name
        self.age = age

    def eat(self):
        print("狗在啃骨头")


# 实例化Cat时 会调用Animal类的__init__方法 故要传color参数
cat = Cat("黄色")
# 拥有 继承 得到 Animal类中的所有方法
print(cat.color)
cat.eat()
cat.run()

# 调用的是Dog里面的方法
dog = Dog("胡狗", 10, "茶色")

# 当子类的方法和父类的方法重名时优先调用子类的方法
dog.eat()
# 先找子类 没有-->找父类 有-->调用
# 先找子类 有-->调用
dog.run()

# 类的多态
# 一个对象拥有多种形态
# obj 自动调用 各种不同类的方法
# 不确定调用哪个类


def feed(obj):
    obj.eat()


an = Animal("黄")
cat = Cat("橙色")
dog = Dog("小黑", 2, "黑色")

feed(cat)
