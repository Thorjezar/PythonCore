#coding=utf-8

'''

装饰器是在函数内部定义一个闭包
调用的使用需要从外面传入一个函数名

'''

def w1(func):
    def inner():
        print("---正在获取权限---")
        func()
    return inner

# 只要python解释器执行到了这个代码，那么就会自动的进行装饰，而不是等到调用的时候才装饰
@w1
def f1():
    print("---f1---")


def f2():
    print("---f2---")

#f2 = w1(f1)
#f2()
#在调用f1之前，已经进行了装饰了
f1()
