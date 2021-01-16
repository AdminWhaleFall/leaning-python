import socket

# 构造对象
server = socket.socket()

# 绑定监听的对象 和客户端保持一致
server.bind(('localhost', 9090))

# 监听
server.listen()
print("准备接电话")

# 等待消息 接收两个返回值
con, addr = server.accept()
print(con, addr)

# 接收 每次最大字节 从二进制 转码
data = con.recv(1024)
print("接收到的消息是:", data.decode())

# 关闭连接
server.close()
