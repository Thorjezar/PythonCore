from multiprocessing import Pool
from time import sleep
import os

def test():
    print('---进程池中的进程---pid=%d,ppid=%d'%(os.getpid(), os.getppid()))
    for i in range(3):
        print('---%d---'%i)
        sleep(1)
    return '回调值'

def test2(args):
    print('---回调函数---pid=%d'%os.getpid())
    print('---回调函数的args=%s'%args)

pool = Pool(3)
pool.apply_async(func=test, callback=test2)

sleep(5)

print('---主进程-pid-%d'%os.getpid())
