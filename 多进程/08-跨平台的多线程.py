from multiprocessing import Process
from time import sleep

def test():
    while True:
         print('---test---')
         sleep(2)

p = Process(target=test) # 初始化Process对象，就是创建一个子进程
p.start()  # 开始这个子进程

def main():
    while True:
        print('---main---')
        sleep(3)

if __name__=='__main__':
    main()
