"""

使用Thread的子类创建子线程
僵尸进程：子进程执行完毕后，父进程没有对其进行内存回收的这一阶段
孤儿进程：子进程还未结束，父进程已经结束了。孤儿进程会被系统中的1号进程最终执行。
linux系统中 0号进程负责切换CPU 1号进程负责创建与回收其他进程

"""
from threading import Thread
from time import sleep

class MyThread(Thread):
    def run(self):
        for i in range(3):
            sleep(1)
            msg = "I'm"+self.name+' @'+str(i)
            print(msg)

def test():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__=="__main__":
    test()
