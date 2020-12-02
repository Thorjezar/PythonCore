#coding=utf-8

'''

常用的专有属性
__getattribute__ 属性访问拦截器
__init__ 初始化函数
__new__ 生成实例所需属性
__str__ 实例字符串表示
__del__ 析构函数 删除对象时调用


'''
class Itcast(object):
    def __init__(self, subject1):
        self.subject1 = subject1
        self.subject2 = "cpp"
    
    # 属性访问拦截器，打log时可以使用
    def __getattribute__(self, sub1):
        print('--------->',sub1)
        if sub1 == 'subject1':
            print('log subject1')
            return sub1
        else:   # 注释掉这两行后找不到subject2
            temp = object.__getattribute__(self, sub1)
            print('-------->',temp)
            return temp

    def show(self):
        print('This is Itcase')

Itcase1 = Itcast('python')
Itcase1.show()
print(Itcase1.subject1)
print(Itcase1.subject2)


