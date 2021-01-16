#队列Queue
import queue

#Queue是python标准库中的线程安全的实现,
#提供了一个适用于多线程编程的先进先出的数据结构，
#即队列，用来在生产者和消费者线程之间的信息传递。

#对于资源，加锁是个重要的环节。
#因为python原生的list,dict等，都是非线程安全的。
#而Queue，是线程安全的，因此在满足使用条件下，建议使用队列。


#创建队列
q=queue.Queue(maxsize=10)


for i in range(1,11):
    q.put(i) #往队列里面放值


# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())

#判断队列是否为空，循环取出所有值
while not q.empty():
    print(q.get())
