# coding=utf-8

'''

动态编程语言 是 高级程序设计语言 的一个类别，在计算机科学领域已被广泛应用。它是一类 在运行时可以改变其结构的语言 ：例如新的函数、对象、甚至代码可以被引进，已有的函数可以被删除或是其他结构上的变化。动态语言目前非常具有活力。例如JavaScript便是一个动态语言，除此之外如 PHP 、 Ruby 、 Python 等也都属于动态语言，而 C 、 C++ 等语言则不属于动态语言。----来自 维基百科




'''
class Person(object):
    def __init__(self, new_name, new_age):
        self.name = new_name
        self.age= new_age


laowang = Person('老王',55)
print(laowang.name)
laowang.addr = '北京...'
print(laowang.age)
print(laowang.addr)

laozhao = Person('老赵',33)
# print(laozhao.addr)

Person.num = 100
print(laowang.num)
print(laozhao.num)
    
