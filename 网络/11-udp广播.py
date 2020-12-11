"""

使用udp协议进行网络广播,地址填写192.168.1.255
这个是广播地址

"""
from socket import *
from threading import Thread
from time import sleep
import sys

def sendto():
    dest = ('<broadcast>', 7788) # 这里是绑定网络广播地址
    # 创建udp套接字
    s = socket(AF_INET, SOCK_DGRAM)
    # 对这个需要发送广播数据的套接字进行修改设置，否则不能发送广播数据
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    while True:
        # 以广播的形式发送数据到本网络的所有电脑中
        s.sendto(b"Hi~who is here?", dest)
        sleep(1)

    while True:
        (buf, address) = s.recvfrom(2024)
        print("收到的%s:%s"%(address, buf))
        sleep(1)

def main():
    print("等待对方回复")

if __name__=="__main__":
    t = Thread(target=sendto)
    t.start()
    main()
    t.join()
