'''
fork只有在类linux或unix系统才有

'''
import os

ret = os.fork()
print(ret)
if ret>0:
    print('---父进程--%d-'%os.getpid()) # 父进程中fork的返回值，就是刚刚创建出来的子进程的id
else:
    print('---子进程--%d--%d'%(os.getpid(), os.getppid()))

