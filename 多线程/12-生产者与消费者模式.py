from threading import Thread
from time import sleep
from queue import Queue

class Producer(Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 1000:
                for i in range(100):
                    count = count + 1
                    msg = '生成产品'+str(count)
                    queue.put(msg)
                    print(msg)
            sleep(0.5)

class Customer(Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    msg = self.name + '消费了' + queue.get()
                    print(msg)
            sleep(0.5)

        
if __name__=='__main__':
    queue = Queue()

    for i in range(500):
        queue.put('初始产品'+str(i))

    for i in range(2):
        p = Producer() # 创建一个Producer类的实例
        p.start() # 开启一个子线程

    for i in range(5):
        c = Customer() # 创建一个Customer类的实例 
        c.start() # 开启一个子线程
