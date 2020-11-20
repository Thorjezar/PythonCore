#coding=utf-8

'''

property属性的使用
方法一 对方法的简单封装
方法二 装饰器

'''

class Demo(object):
    
    def __init__(self):
        self.__num = 100

    @property
    def num(self):
        print("----getter----")
        return self.__num
    
    @num.setter
    def num(self, newNum):
        print("----setter----")
        self.__num = newNum


demo = Demo()
print(demo.num)
demo.num = 200
print(demo.num)
