# coding=utf-8

'''

动态编程语言 是 高级程序设计语言 的一个类别，在计算机科学领域已被广泛应用。它是一类 在运行时可以改变其结构的语言 ：例如新的函数、对象、甚至代码可以被引进，已有的函数可以被删除或是其他结构上的变化。动态语言目前非常具有活力。例如JavaScript便是一个动态语言，除此之外如 PHP 、 Ruby 、 Python 等也都属于动态语言，而 C 、 C++ 等语言则不属于动态语言。----来自 维基百科


'''
import types

class Person(object):

    speed = 0

    def __init__(self, new_name, new_age):
        self.name = new_name
        self.age= new_age
        
    def eat(self):
        print("吃")

def run(self):
    print("跑")

@classmethod
def testSpeed(cls):
    cls.speed = 100

@staticmethod
def testStatic():
    print("-----static method----")



p1 = Person("p1",10)
p1.eat()

# p1.run = run
# p1.run()    # 直接去动态设置对象的方法不可以，需要导入types模块

p1.run = types.MethodType(run, p1) # 给实例添加方法，动态添加
p1.run()

# 给类绑定给方法
Person.testSpeed = testSpeed
# 调用类属性
print(Person.speed)
Person.testSpeed()
print(Person.speed)

# 给类对象绑定静态方法
Person.testStatic = testStatic
# 调用
Person.testStatic()
