# 使用了线程库
import threading
# 队列
import queue
import requests
import time

# https://www.qiushibaike.com/8hr/page/1/
# https://www.qiushibaike.com/8hr/page/2/
# https://www.qiushibaike.com/8hr/page/3/

#采集网页线程--爬取段子列表所在的网页，放进队列
class Thread1(threading.Thread):
    def __init__(self, threadName,pageQueue,dataQueue):
        threading.Thread.__init__(self)
        self.threadName = threadName #线程名
        self.pageQueue = pageQueue #页码队列
        self.dataQueue = dataQueue #数据队列
        self.headers = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}


    def run(self):
        print("启动线程"+self.threadName)
        while not flag1:
            try:
                page=self.pageQueue.get()
                url="https://www.qiushibaike.com/8hr/page/"+str(page)+"/"
                content=requests.get(url,headers=self.headers).text
                time.sleep(0.5)
                self.dataQueue.put(content) #将数据放入数据队列中
            except Exception as e:
                pass
        print("结束线程"+self.threadName)

#解析网页线程--从对、队列中拿到列表网页，进行解析，并存储到本地
class Thread2(threading.Thread):
    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.threadName = threadName

    def run(self):
        print("启动线程"+self.threadName)
            #-------
        print("结束线程"+self.threadName)

flag1=False
flag2=False


def main():
    #页码队列
    pageQueue=queue.Queue(10)

    for i in range(1,11):
        pageQueue.put(i)

    dataQueue=queue.Queue()

    filename=open(r"C:\file\dianzi.txt","a")



if __name__ == '__main__':
    main()
