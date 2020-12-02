import os
import time

ret = os.fork()
if ret == 0:
    while True:
        print("子进程1")
        time.sleep(1)
else:
    while True:
        print("父进程")
        time.sleep(2)

