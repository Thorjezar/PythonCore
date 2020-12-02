from threading import local
from threading import Thread
import threading

#创建全局ThreadLocal对象:
local_school = local()

def process_student():
    std = local_school.student
    print('Hello, %s (in %s)'%(std, threading.current_thread().name))

def process_thread(name):
    local_school.student = name # 给local对象添加了一个属性，并赋值name
    process_student()

t1 = Thread(target= process_thread, args=('A'), name='Thread-A')
t2 = Thread(target= process_thread, args=('B'), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
