from multiprocessing import Process
from time import sleep

class Process_class(Process):
    def run(self):
        while True:
            print('---1---')
            sleep(1)

p = Process_class()
p.start()

while True:
    print('---main---')
    sleep(1)
