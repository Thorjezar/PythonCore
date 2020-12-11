"""
echo服务器:接收到的数据再原路返回给发送方
可以将这个作为中转服务来使用,一个接收和处理 再输出到其他方法中
"""
from socket import *

def main():
    UdpSocket = socket(AF_INET, SOCK_DGRAM)

    UdpSocket.bind(("", 7788))
    num = 1 # 计数标致位
    while True:
        # 接收数据
        recvData = UdpSocket.recvfrom(1024)
        content, Ipaddr = recvData
        # 再将数据原路返回
        UdpSocket.sendto(content, Ipaddr)

        print('将第%d条数据返回，内容是：%s'%(num, content))
        num +=1

if __name__=="__main__":
    main()
