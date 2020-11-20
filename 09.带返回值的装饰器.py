#coding=utf-8

'''

带参数的装饰器，需要在内部的闭包函数中传入参数
无参数的装饰器，不需要在内部传参

'''

def demo(functionName):
    print("-"*4 + "1" + "-"*4)
    def inner_demo():
        print("-"*4 + "2" + "-"*4)
        ret = functionName()
        print("-"*4 + "3" + "-"*4)
        return ret
    return inner_demo

@demo
def test():
   print("-"*3 + "test" + "-"*3)
   return "haha"

ret = test()
print("return value is %s"%ret)

