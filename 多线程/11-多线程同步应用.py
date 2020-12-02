from threading import Thread
from threading import Lock
from time import sleep

class Task1(Thread): # 调用Thread的子类实现子线程
    def run(self):
        while True:
            if lock1.acquire(): # 给锁一上锁
                print('---Task1---')
                sleep(0.5)
                lock2.release() # 给锁二解锁

class Task2(Thread):
    def run(self):
        while True:
            if lock2.acquire(): # 给锁二上锁
                print('---Task2---')
                sleep(0.5)
                lock3.release() # 给锁三解锁

class Task3(Thread):
    def run(self):
        while True:
            if lock3.acquire(): # 给锁三上锁
                print('---Task3---')
                sleep(0.5)
                lock1.release() # 给锁一解锁


if __name__=="__main__":
    lock1 = Lock()
    lock2 = Lock()
    lock3 = Lock()
    #将锁2和锁3上锁
    lock2.acquire()
    lock3.acquire()
    #开启新的子线程
    t1 = Task1()
    t2 = Task2()
    t3 = Task3()

    t1.start() # 开启子线程
    t2.start()
    t3.start()
