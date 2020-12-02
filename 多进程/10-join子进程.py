from multiprocessing import Process
from time import sleep
from random import randint

def test():
    for i in range(randint(1, 5)):
        print("----%d----"%i)
        sleep(1)

p = Process(target=test)
p.start()

p.join(1) # 等到子进程结束之后，主进程才继续往下走;堵塞

print("----main----")

