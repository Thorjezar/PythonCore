'''

进程与进程之间的全局变量或者数据互不共享，在各自的进程中各不一样。
进程之间的通信
网络是不同设备的进程之间的通信

'''
import os
import time

g_num = 100

ret = os.fork()
if ret == 0:
    print('----process-1----')
    g_num +=1
    print('----process-1 g_num=%d-'%g_num)
else:
    time.sleep(3)
    print('----process-2----')
    print('----process-2 g_num=%d-'%g_num)

