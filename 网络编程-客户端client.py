# socket (插孔) 嵌套字
#客户端
import socket
import time
client=socket.socket()
client.connect(('localhost',9090))
while True:
	#生成socket连接对象
	# client=socket.socket()

	#和目标主机建立连接 localhost本机 动态端口
	# client.connect(('localhost',9090))


	#向对方发送信息 Python3里边要转成二进制格式(编码)
	client.send("我爱你".encode())

	#关闭连接
	client.close()
	time.sleep(12)


