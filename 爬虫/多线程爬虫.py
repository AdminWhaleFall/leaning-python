import threading #多线程
import time

def run(name):
    print(name,"线程执行了")
    time.sleep(5)

#创建线程
t1=threading.Thread(target=run,args=("t1",))
t2=threading.Thread(target=run,args=("t2",))

#启动子线程 并行执行
t1.start()
t2.start()

#等待子线程执行完毕后再执行主线程后面的内容
t1.join()
t2.join()

print("执行完毕")











