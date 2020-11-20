#coding=utf-8

'''

带参数的装饰器，需要在内部的闭包函数中传入参数
无参数的装饰器，不需要在内部传参

'''

#def demo(test):
#    print("-"*4 + "1" + "-"*4)
#    def inner_demo():
#        print("-"*4 + "2" + "-"*4)
#        test()
#        print("-"*4 + "3" + "-"*4)
#    return inner_demo
#
#@demo
#def test():
#    print("-"*3 + "test" + "-"*3)
#
#test()

def demo2(functionName):
    print("-"*4 + "1" + "-"*4)
    def inner_demo(*args, **kwargs):
         print("-"*4 + "2" + "-"*4)
         functionName(*args, **kwargs)
         print("-"*4 + "3" + "-"*4)
    return inner_demo

@demo2
def test2(a, b, c):
    print("-----a=%d,b=%d,c=%d-----"%(a, b, c))

@demo2
def test3(a, b, c, d):
    print("----a=%d,b=%d,c=%d,d=%d----"%(a, b, c, d))

test2(11,22,33)
test3(44,55,66,77)
