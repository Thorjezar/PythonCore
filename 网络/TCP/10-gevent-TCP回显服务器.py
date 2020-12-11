"""

gevent版的TCP服务器，用协程来创建多任务的服务器


"""
from gevent import socket
from gevent import monkey
from time import sleep

import gevent
import sys

def handle_info(client):
    while True:
        data = client.recv(1024)
        if not data:
            print("客户%s 已退出"%str(clientList[client]))
            del clientList[client]
            client.close()
            break
        print("收到信息：", data)
        client.send(data)

clientList = {}

def main(port):
    serverSocket = socket.socket()
    serverSocket.bind(("", port))
    serverSocket.listen(5)
    while True:
        client, addr = serverSocket.accept()
        print("新的客户端链接:%s"%str(addr))
        clientList[client] = addr
        gevent.spawn(handle_info, client)

if __name__=="__main__":
    main(7790)
