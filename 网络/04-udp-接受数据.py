#coding=utf-8

from socket import *
# 使用UDP发送数据，每次都要写接受方的IP和port UPD-DGRAM TCP-STREAM 
udpSocket = socket(AF_INET, SOCK_DGRAM)
# 绑定端口，没有写ip地址表示，本电脑上的任何IP地址下的port都可以
# 一般情况下，接受方需要绑定。发送方不需要访问
udpSocket.bind(('', 19823))
# python3中 发送字符串 前面要加b
#udpSocket.sendto(b"haha", ("192.168.136.1", 8080))

# 接受套接字信息
recvData = udpSocket.recvfrom(1024) # 写1024表示每次最大接受的字节数

print(recvData)

