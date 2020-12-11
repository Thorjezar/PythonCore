"""
进程池pool的多进程TCP服务端

"""
from socket import *
from multiprocessing import Pool

def deal_info(socket, address):
    while True:
        recvData = socket.recv(1024)
        if len(recvData)>0:
            print("客户端~%s:%s"%(str(address), recvData.decode("gb2312")))
        else:
            print("客户端~%s已经关闭"%str(address))
            break
    # 如果没有数据了 关闭这个客户端的套接字
    socket.close()

def main():
    # 创建服务端套接字
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # 绑定地址
    addr = ("", 7789)
    serverSocket.bind(addr)

    # 当服务端重启或者主动调用close时，为了端口能够重复使用
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # 被动监听的套接字，用来等待被客户端唤醒
    serverSocket.listen(5)

    # 创建进程池
    pool = Pool(20)
    try:
        while True:
            print("----主进程等待新的子进程接入----")
            # 主进程等待接收新的客户端请求
            clientSocket, clientAddress = serverSocket.accept()
            print("----主进程创建新的子进程来处理客户端%s"%str(clientAddress))
            # 异步调用接收打印方法
            pool.apply_async(deal_info, (clientSocket, clientAddress, ))
            # 因为进程会拷贝资源到子进程，所以主进程关闭客户端不会影响到子进程
            #clientSocket.close()
    finally:
        # 关闭服务器端
        serverSocket.close()
        pool.close() # 关闭进程池pool，关闭后不再接收新的子进程
        pool.join() # 主进程等待所有子进程执行完成，必须放在close后面
        print("关闭服务器")

if __name__=="__main__":
    main()
