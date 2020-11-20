#coding=utf-8

'''

property属性的使用
对方法的简单封装

'''

class Demo(object):
    
    def __init__(self):
        self.__num = 100

    def getNum(self):
        print("----getter----")
        return self.__num
    
    def setNum(self, newNum):
        print("----setter----")
        self.__num = newNum

    num = property(getNum, setNum) # 用属性的方式，掩盖调用内部函数的方式

demo = Demo()
print(demo.num)
demo.num = 200
print(demo.num)
