#coding=utf-8

"""
创建tcp的服务端

"""
from socket import *
from time import sleep

# 创建套接字对象
serverSocket = socket(AF_INET, SOCK_STREAM)

# 绑定地址
bind_addr = ("", 7788)
serverSocket.bind(bind_addr)

listen_num = int(input("请输入链接到服务端的最大值:"))

# 将套接字变为监听状态
serverSocket.listen(listen_num)

for i in range(10):
    print i
    sleep(1)

while True:
    newSocket, clientAddr = serverSocket.accept() # 不停的接受新的客户端链接
    print clientAddr
    sleep(1)
