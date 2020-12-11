"""

TCP服务端 设置
共分为5步

第一创建套接字
第二绑定
第三监听
第四接收
第五关闭

"""

from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM) # 定义tcp的套接字

serverSocket.bind(("", 7789)) # 绑定ip和端口号

serverSocket.listen(5) # 监听 将主动的socket变为被动监听模式,参数5表示tcp的半链接和全链接个数综合
# 在类linux系统中，监听值是由系统去决定，这个值是系统计算出来的
print("----1----")
clientSocket, clientAddre = serverSocket.accept() # 接受到的消息，可以进行返回值的处理，返回的是元组数据(客户端，客户端的地址)

print("----2----")
result = clientSocket.recv(1024) # 客户端发来的信息

print("----3----")
print("%s:%s"%(clientAddre, result))

clientSocket.close() # 关闭套接字
serverSocket.close() # 关闭套接字


