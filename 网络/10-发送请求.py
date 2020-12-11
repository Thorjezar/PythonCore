#coding=utf-8
"""


大端和小端的区别
大端高地址存储高位数据 0x1122 
小端高地址存低位数据 0x2211

网络中传输数据都要以大端形式传输0x1122这样的

"""


import struct
from socket import *

# 开始构建网络上传的数据格式 叹号表示这个数据要上传网络
# H表示要占两位字节
# 8s表示 test.jpg 替换
# b 表示 一个字节0
# 5s表示 octet

sendData = struct.pack("!H8sb5sb",1,"test.png",0,"octet",0)

udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.sendto(sendData, ("192.168.3.4", 69))

recvInfo = udpSocket.recvfrom(1024)
#print(recvInfo)
#content, ipaddr = recvInfo
#print(content.decode())  # 解包的时候用什么格式？用unpack
#print(ipaddr)
result = struct.unpack("!HH", recvInfo[0][:4]) # HH代表收到网络上的4个字节，把两个字节当成一个数据输出
print(result[0],result[1]) # 返回的是一个元组

udpSocket.close()
