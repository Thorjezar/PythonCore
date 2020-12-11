"""

多进程Process的TCP服务器


"""
from socket import *
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self, socket, address):
        super().__init__()
        self.clientsocket = socket
        self.clientaddress = address
    
    def run(self):
        while True:
            recvData = self.clientsocket.recv(1024)
            if len(recvData)>0:
                print("客户端~%s:%s"%(str(self.clientaddress), recvData.decode("gb2312")))
            else:
                print("客户端~%s已经关闭"%str(self.clientaddress))
                break
        self.clientsocket.close()

def main():
    # 创建服务端的TCP套接字
    serverSocket = socket(AF_INET, SOCK_STREAM)
    
    # 要绑定的本地IP以及端口初始化
    local_address = ("", 7788)
    
    # 参数1表示，服务器在主动调用close()关闭套接字后，无需再等待TCP的2MSL时间段
    # 达到重复使用绑定的信息
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    
    # 绑定服务器的地址
    serverSocket.bind(local_address)
    
    # 变为被动套接字，进行客户端访问的接收
    serverSocket.listen(5)
    try:
        while True:
            print("----主进程，等待新客户端的请求----")
            clientSocket, clientAddress = serverSocket.accept() # 循环的接受客户端套接字链接
            
            print("----主进程,创建新的子进程去处理客户端%s"%str(clientAddress))
            client = MyProcess(clientSocket, clientAddress)
            client.start()
            
            # 子进程独立拥有客户端线程的资源，所以主进程可以关闭这个子进程而不会影响到子进程使用
            clientSocket.close()
    finally:
        # 当所有的客户端服务完之后再进行关闭套接字
        serverSocket.close()
        print("关闭服务端")

if __name__=="__main__":
    main()
