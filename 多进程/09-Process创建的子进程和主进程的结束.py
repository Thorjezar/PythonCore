"""
利用Process创建的子进程对象，主进程会等待所有的子进程内执行完毕才会退出

"""
from multiprocessing import Process
from time import sleep

def test():
    for i in range(5):
         print('---test---')
         sleep(1)

p = Process(target=test) # 初始化Process对象，就是创建一个子进程
p.start()  # 开始这个子进程
