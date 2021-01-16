# 电脑单核CPU每次只能运行一个进程中的一个线程
# 多个进程的运行其实是 上下文切换
# 进程中可以包含多个线程 上下文切换 同时执行
import threading  # 多线程模块
import time


def run(name):
    print(name, "线程执行了")
    time.sleep(10)


# 建立两个线程 target=要执行的方法名 args=变量序列(要加,)
t1 = threading.Thread(target=run, args=("线程t1",))
t2 = threading.Thread(target=run, args=("线程t2",))

# 程序执行时,本身就是一个线程,叫主线程
# 手动创建的线程,叫子线程
# 主线程的执行中不会等待子线程执行完成,就会直接执行后面的代码

# 启动线程 同时并行地执行 上下文切换
# t1.start()
# t2.start()

# t1.join() #等待子线程执行完毕后再执行主线程的内容
# t2.join()

# print("执行完毕！")

# 线程锁
# 补充: 全局变量:作用域是整个程序,全局范围内可以使用(一般用大写字母表示)
# 局部变量:作用域是某个函数,只能在函数内部使用(一般用小写字母表示)
# 若在函数内部，如果局部变量与全局变量变量名一样，则优先调用局部变量。
# 如果想在函数内部改变全局变量,需要在前面加上global关键字,在执行函数之后,全局变量值也会改变。
# 若全局变量是列表的话就不用加上global关键字

'''
def test():
	global a
	a=2
	# return a
test()
print(a) #报错:NameError: name 'a' is not defined
'''

summm = 0
# 可以发现有些线程没有执行完整就直接跑到下个线程里边去了,故要 线程锁
# 创建一个线程锁 互斥锁 解决对资源同时访问容易乱套的问题

'''
lock=threading.Lock()

def summ(name):
	lock.acquire() #为线程上锁
	global summm  #设置summ为全局变量,以修改summ的数值
	summm=summm+1
	print("线程",name,"执行了,目前summm的值为:",summm)
	lock.release() #释放线程锁

#用for循环创建100个线程,并同时开始
for i in range(0,100):
	t=threading.Thread(target=summ,args=(i+1,))
	t.start()
'''

# 全局解释器锁(GIL) Python内部的锁
# 不管系统CPU核心数量是多少,
# 都保证py程序同一时间点只能执行一个线程
# 使用多进程解决GIL问题
