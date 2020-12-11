from socket import *

UpdSocket = socket(AF_INET, SOCK_DGRAM)

ipaddress = input('请输入要传递数据的地址:')
iport = int(input('请输入要传输数据的端口号:'))
content = input('请输入要传送数据的内容:')

# 发送数据时进行编码
#UpdSocket.sendto(content.encode('utf-8'), (ipaddress, iport))

# 发送到的网络调试助手是用gb2312来进行解码的
UpdSocket.sendto(content.encode('gb2312'), (ipaddress, iport))


