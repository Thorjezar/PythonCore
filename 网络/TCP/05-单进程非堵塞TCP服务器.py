"""
采用socket的非堵塞特征，使用单进程模拟多进程
TCP服务器

"""
from socket import *

def main():
    # 创建网络套接字TCP协议
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # 绑定服务器的ip和port
    addr = ("", 7789)
    serverSocket.bind(addr)
    # 可以重复利用端口
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 利用socket的非堵塞模式
    # 如果accept没有收到connect请求，那么这个会产生一个异常
    serverSocket.setblocking(False)
    # 设置socket的监听，被动套接字
    serverSocket.listen(5)
    
    clientList = []

    while True:
        try:
            # 循环接收客户端的请求,如果没有请求那么就继续循环
            clientSocket, clientAddress = serverSocket.accept()
        except:
            pass
        else:
            print("一个新客户端%s链接"%str(clientAddress))
            clientSocket.setblocking(False) # 将客户端套接字设置为非堵塞，为了后面的接受信息
            clientList.append((clientSocket, clientAddress)) # 保存客户端信息

        for client,address in clientList:
            try:
                recvData = client.recv(1024)
            except:
                pass
            else:
                if len(recvData)>0:
                    print("客户端~%s:%s"%(str(address), recvData.decode("gb2312")))
                else:
                    client.close()
                    print("客户端%s已经退出"%str(address))
                    clientList.remove((client, address))


if __name__=="__main__":
    main()
