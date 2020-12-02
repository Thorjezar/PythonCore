from multiprocessing import Pool
from time import sleep
import os

# 每个进程添加的任务，执行了一次打印，结果来看是顺序执行
def work_er(num):
    print("---num=%d-pid=%d"%(num, os.getpid()))
    sleep(1)

# 每个进程添加的任务，循环5次执行打印，结果来看，除了有顺序执行外，还包含有
def work_ers(num):
    for i in range(5):
        print("---pid=%d--num=%d--i=%d"%(os.getpid(), num, i))
        sleep(1)

po = Pool(3) # 创建进程池 最大进程数为3

# 定义10个任务添加到进程池创建的进程中
for i in range(10):
    print('----%d----'%i)
    # 向进程添加任务
    # 每个进程的pid是在开始创建好的，执行完一个任务后，会接着执行下一个任务
    po.apply(work_ers, (i,))
    po.apply(work_er, (i,))

po.close() # 关闭进程池，也就是说停止再往进程池内添加任务
po.join() # 主进程等待 进程池中的子进程完全执行完毕后，再退出。如果不添加join() 程序会直接退出
