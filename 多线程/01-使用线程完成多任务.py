"""
进程是代码添加到内存中后，系统为其分配的资源---属于资源调度

进程在执行时，一定会有一个主线程（箭头）去执行代码---属于CPU执行调度
线程是在同一资源（进程）下去执行多任务的一种方式
当遇到Thread时，会创建出主线程的子线程，这时主线程被成为父线程。
使用Thread创建线程还有一个特点是，父线程会判断子线程是否结束，只有所有的子线程结束，父线程才会结束

"""

from time import sleep
from threading import Thread

#1.如果多个线程执行的同一个函数的话，各自之间不会影响
def test():
    print('---test--')
    sleep(1)

if __name__=='__main__':
   for i in range(5):
       t1 = Thread(target=test)
       t1.start()

