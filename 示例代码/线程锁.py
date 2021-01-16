import threading

lock=threading.Lock()#创建一个线程锁（互斥锁）
num=100

def run(name):
	lock.acquire() #设置锁
	global num #设置num为全局变量
	num=num-1
	print("线程",num,"执行了，目前num的值为：",num)
	lock.release() #释放锁

#创建并启动100个线程
for i in range(100):
	t=threading.Thread(target=run,args=(i+1,))
	t.start()


#全局解释器锁（GIL）
#不管系统cpu核心数量是多少，
#都保证python程序中同一时间点只能执行一个线程
#使用多进程解决GIL所造成的问题




