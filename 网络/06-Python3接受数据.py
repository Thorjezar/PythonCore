from socket import *

UpdSocket = socket(AF_INET, SOCK_DGRAM)

bindAddress = ("", 7788)
UpdSocket.bind(bindAddress)

recvData = UpdSocket.recvfrom(1024)
content, sendAddress = recvData

print('content is %s'%content)
# 使用utf-8格式进行解码 或者使用gb2312解码
print('content is decode %s'%content.decode('gb2312'))

