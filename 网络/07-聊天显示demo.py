from socket import *
def main():
    # 创建网络套接字
    UpdSocket = socket(AF_INET, SOCK_DGRAM)
    # 绑定端口号
    bindAddress = ("", 7788)
    UpdSocket.bind(bindAddress)

    # 接收消息 循环接收展示
    while True:
        recvData = UpdSocket.recvfrom(1024)
        content, Ipaddr = recvData
        print("[%s~%d]发送了:%s"%(Ipaddr[0], Ipaddr[1], content.decode('gb2312')))

if __name__=='__main__':
    main()
