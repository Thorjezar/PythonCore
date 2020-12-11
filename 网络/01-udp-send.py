#coding=utf-8

from socket import *
# 使用UDP发送数据，每次都要写接受方的IP和port
udpSocket = socket(AF_INET, SOCK_DGRAM)
# python3中 发送字符串 前面要加b
udpSocket.sendto(b"haha", ("192.168.136.1", 8080))
udpSocket.sendto(b"haha1", ("192.168.136.1", 8080))
