#coding=utf-8

'''

gc的demo
搞清gc的垃圾回收机制，引用计数 零代回收
不用自己去定义新的回收机制

在类中定义__del__() 方法后，要在内部添加object的gc回收功能，否则gc无法自动删除占用的内存空间

'''

import gc

class Demo(object):
    def __init__(self):
        print("Object is born,id:%s"%str(hex(id(self))))


def f2():
    while True:
        a = Demo()
        b = Demo()
        a.t1 = b
        b.t1 = a
        del a
        del b
        gc.collect()

gc.disable()
f2()
