import threading

lock=threading.Lock()
num=100

#卖票
def sale(name):
	lock.acquire()
	global num
	if num>0:
		num=num-1
		print(name,"卖出一张票，还剩",num,"张！")
	lock.release()


#售票窗口（2个线程表示）
while 1==1:
	if num>0:
		ta=threading.Thread(target=sale,args=("A窗口",))
		tb=threading.Thread(target=sale,args=("B窗口",))
		ta.start()
		tb.start()
	else:
		break
print("票已经卖完！")



