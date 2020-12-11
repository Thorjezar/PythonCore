"""
全双工的通信

"""
from threading import Thread
from socket import *
from time import sleep

# 接收数据，并且打印
def recvData(udpsocket):
    while True:
        recvInfo = udpsocket.recvfrom(1024) # 命名不要和函数同名
        recontent, reipaddr = recvInfo
        print('\r>>[%s~%d]:%s'%(reipaddr[0], reipaddr[1], recontent.decode("gb2312"))) # 解码用gb231
        print('\r>>',end="") # 起到了下一行的时候，换行输出>> 同时光标紧跟在后面

# 发送数据，并且监控键盘的输入
def sendData(udpsocket, ipaddr, iport):
    sendAddr = (ipaddr, iport)
    while True:
        content = input('\r<<')
        udpsocket.sendto(content.encode("gb2312"), sendAddr) # 通用型的编码用utf-8 演示demo用gb2312

# 主程序，分别建立两个线程去收和发数据
def main():
    udpsocket = socket(AF_INET, SOCK_DGRAM)
    ipaddr = input('请输入对方ip：')
    iport = int(input('请输入对方端口:'))

    localPort = int(input('请输入本机的端口：'))
    udpsocket.bind(('', localPort))

    t1 = Thread(target=sendData, args=(udpsocket, ipaddr, iport, ))
    t2 = Thread(target=recvData, args=(udpsocket, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
