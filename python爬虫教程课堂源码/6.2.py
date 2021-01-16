# 使用 threading 模块创建线程 
# 创建一个新的子类继承threading.Thread.
# 并实例化后调用 start() 方法启动新线程，即它调用了线程的 run() 方法

import threading
import time

#线程类
class myThread(threading.Thread):

    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("开始线程",self.name)
        print("线程执行中---1")
        time.sleep(1)
        print("线程执行中---2")
        time.sleep(1)
        print("线程执行中---3")
        time.sleep(1)
        print("线程执行中---4")
        time.sleep(1)
        print("线程执行中---5")
        time.sleep(1)
        print("结束线程",self.name)

#创建线程
t1=myThread("t1")
t2=myThread("t2")
t3=myThread("t3")

#开启线程
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("执行完毕")
