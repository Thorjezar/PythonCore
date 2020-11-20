#coding=utf-8

'''

带有参数的装饰器，需要在闭包的外面再定义一个函数
这个函数返回定义闭包的函数体名的引用。

'''
#1.先执行demo_arg("hehe")函数，这个函数return 结果是demo这个函数的引用
#2.@demo
#3.使用@demo对test进行装饰

def demo_arg(arg):
    def demo(functionName):
        def inner_demo():
             print("---记录日志---arg=%s"%arg)
             if arg == "hehe":
                 functionName()
                 functionName()
             else:
                 functionName()
        return inner_demo
    return demo

@demo_arg("hehe")
def test():
   print("-"*3 + "test" + "-"*3)
#带有参数的装饰器，能够在运行时起到不同的功能
@demo_arg("haha")
def test2():
   print("-"*3 + "test2" + "-"*3)

test()
test2()
