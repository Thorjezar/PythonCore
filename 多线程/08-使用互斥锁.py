from threading import Thread
from threading import Lock
import time

g_num = 0
def test1():
    global g_num
    #这个线程和test2线程都在抢着 对这个锁进行上锁，如果有1方成功的上锁，那么导致另外的一方
    #会堵塞（一直等待）到这个锁被解开为止
    mutex.acquire() # 互斥锁上锁 
    for i in range(1000000):
         g_num += 1
    mutex.release() # 互斥锁解锁

    print("---test1---g_num=%d"%g_num)

def test2():
    global g_num
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    mutex.release()

    print("---test2---g_num=%d"%g_num)

#创建一把互斥锁,默认是没有上锁的
mutex = Lock()

p1 = Thread(target=test1)
p1.start()

p2 = Thread(target=test2)
p2.start()

print("---g_num=%d---"%g_num)
