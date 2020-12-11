from time import sleep

def A():
    while True:
        print("----A----")
        yield # 协程堵塞在这条语句之后
        sleep(0.5)

def B(c):
    while True:
        print("----B----")
        c.__next__() # 调用生成器
        sleep(0.5)

if __name__=="__main__":
    a = A()
    #a.__next__()
    B(a)

