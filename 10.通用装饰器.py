#coding=utf-8

'''

带参数的装饰器，需要在内部的闭包函数中传入参数
无参数的装饰器，不需要在内部传参
所谓的通用装饰器，就是有传入的参数和返回值

'''

def demo(functionName):
    def inner_demo(*args, **kwargs):
        print("-"*4 + "记录日志" + "-"*4)
        ret = functionName(*args, **kwargs)
        return ret
    return inner_demo

@demo
def test():
   print("-"*3 + "test" + "-"*3)
   return "haha"

@demo
def test2():
   print("-"*3 + "test2" + "-"*3)

@demo
def test3(a, b, c): 
   print("--a=%d,b=%d,c=%d----"%(a, b, c))

@demo
def test4(a, b, c):
    print("--a=%d,b=%d,c=%d----"%(a, b, c))
    return a + b + c

ret = test()
print("return value is %s"%ret)

test2()

test3(11,22,33)

a = test4(111,222,333)
print("a+b+c=%d"%a)
