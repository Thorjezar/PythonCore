from threading import Thread
import threading
from time import sleep


def test1():
    name = threading.current_thread().name
    g_num=100
    if name == 'Thread-1':
        g_num+=1
        sleep(1)
    else:
        sleep(2)
    print("---Thread is %s---g_num=%d"%(name, g_num))

#def test2():
#    print("---test2---g_num=%d"%g_num)


p1 = Thread(target=test1)
p1.start()


p2 = Thread(target=test1)
p2.start()

