import os

ret_1 = os.fork()
print(ret_1)
if ret_1 == 0:
    print('-子进程1-(%d)-我的父进程是(%d)'%(os.getpid(), os.getppid()))
else:
    print('-父进程2-(%d)'%os.getpid())

ret_2 = os.fork()
if ret_2 == 0:
    print('-子进程11-(%d)-我的父进程是(%d)'%(os.getpid(), os.getppid()))
else:
    print('-父进程22-(%d)-我的父进程是(%d)'%(os.getpid(), os.getppid()))

ret_3 = os.fork()
if ret_3 == 0:
    print('-子进程111-(%d)-我的父进程是(%d)'%(os.getpid(), os.getppid()))
else:
    print('-父进程222-(%d)-我的父进程是(%d)'%(os.getpid(), os.getppid()))
