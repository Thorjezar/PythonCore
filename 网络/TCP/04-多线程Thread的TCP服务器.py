"""

多线程Thread的TCP服务器

"""
from socket import *
from threading import Thread

class MyThread(Thread):
    def __init__(self, socket, address):
        super().__init__()
        self.socket = socket
        self.address = address
    
    # 重写父类的run方法
    def run(self):
        while True:
            recvData = self.socket.recv(1024)
            if len(recvData)>0:
                print("客户端~%s:%s"%(str(self.address), recvData.decode("gb2312")))
            else:
                print("客户端%s已经关闭"%str(self.address))
                break
        # 处理完毕后，关闭套接字
        self.socket.close()

def main():
    # 创建服务器的套接字
    serverSocket = socket(AF_INET, SOCK_STREAM)
    
    # 绑定地址
    addr = ("", 7798)
    serverSocket.bind(addr)
    
    # 服务器端的端口重启
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # 变为被动的套接字,最大连接数量在linux系统中是系统去定义的
    serverSocket.listen(5)

    try:
        while True:
            print("----主进程等待接收新的客户端请求----")
            clientSocket, clientAddress = serverSocket.accept() # 没有收到的话会产生堵塞
            print("----主进程创建新的子线程去处理客户端%s"%str(clientAddress))
            t = MyThread(clientSocket, clientAddress)
            t.start()
    finally:
        # 关闭服务端
        serverSocket.close()
        print("关闭服务器")

if __name__=="__main__":
    main()
