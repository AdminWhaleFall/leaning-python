import threading
import time

def run(name):
	print(name,"线程执行了")
	time.sleep(5)
	
#程序执行时，程序本身就是一个线程，叫主线程
#手动创建的线程，叫子线程
#主线程的执行中不会等待子线程执行完毕，就会直接执行后面的代码
#创建线程
t1=threading.Thread(target=run,args=("t1",))
t2=threading.Thread(target=run,args=("t2",))


t1.start() #启动线程
t2.start()

t1.join()#等待子线程执行完毕之后再执行主线程内容
t2.join()

print("执行完毕")



