from threading import Thread
import time

g_num = 0
g_flag = 1 # 方式二，增加一个判断的标志
def test1():
    global g_num
    global g_flag
    if g_flag == 1:
         for i in range(1000000):
             g_num += 1
        
    g_flag = 0

    print("---test1---g_num=%d"%g_num)

def test2():
    global g_num
    #方法二 轮询:效率太低 不停的占用CPU
    while True:
        if g_flag != 1:
             for i in range(1000000):
                 g_num += 1
             break
    print("---test2---g_num=%d"%g_num)

p1 = Thread(target=test1)
p1.start()

#time.sleep(3) # 方法一：通过增加延迟，让一个子线程先执行完毕后，再执行第二个子线程

p2 = Thread(target=test2)
p2.start()

print("---g_num=%d---"%g_num)
