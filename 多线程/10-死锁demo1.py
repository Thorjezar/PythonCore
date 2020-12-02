from threading import Thread
from threading import Lock
from time import sleep

class MyThread1(Thread):
    def run(self):
        if mutex1.acquire(): # 锁一 上锁 解决死锁的方法一增加超时时间timeout参数
            print(self.name+'---do1---up')
            sleep(1)

            if mutex2.acquire():
                print(self.name+'---do1---down')
                mutex2.release()
            mutex1.release()

class MyThread2(Thread):
    def run(self):
        if mutex2.acquire(): # 锁二 上锁
            print(self.name+'---do2---up')
            sleep(1)
            if mutex1.acquire():
                print(self.name+'---do2---down')
                mutex1.release()

            mutex2.release()

if __name__=="__main__":
    mutex1 = Lock()  # 定义互斥锁一，未上锁
    mutex2 = Lock()  # 定义互斥锁二，未上锁
    t1 = MyThread1() # 定义线程一
    t2 = MyThread2() # 定义线程二 方法二 银行家算法
    t1.start()
    t2.start()
