#服务端
import socket

server=socket.socket() #生成socket连接对象

server.bind(('localhost',6962)) #绑定要监听的对象

server.listen()   #监听

conn,addr=server.accept()  #等待消息

print(conn,addr)

data=conn.recv(1024)

print('接收到的消息:',data)

server.close()
