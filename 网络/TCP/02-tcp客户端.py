"""
tcp客户端建立分三步
第一创建套接字
第二调用链接方法connect
第三关闭套接字

"""

from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM) # 创建客户端的套接字

clientSocket.connect(("192.168.3.4", 8989)) # 链接到服务端

clientSocket.send("haha".encode("gb2312")) # 向服务端发送一个消息

recvData = clientSocket.recv(1024) # 从服务端接收数据

print("收到的信息是%s"%recvData)

clientSocket.close() # 关闭套接字
