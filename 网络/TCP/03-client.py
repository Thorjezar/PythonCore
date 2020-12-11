#coding=utf-8

"""

创建tcp的客户端
来验证多个socket的链接
来验证链接socket的最大值
在同一个进程中，创建socket可以有无数个，这个上限并没有标明

"""
from socket import *

num = int(input("请输入创建套接字的个数:"))

for i in range(num):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    addr = ("127.0.0.1", 7788)
    clientSocket.connect(addr)
    print(i)
