#coding=utf-8

'''

记录一个坑


'''
class Person(object):
    def __getattribute__(self, sub):
        print('---test---')
        if sub.startswith("a"):
            return "haha"
        else:
            return self.test   #  记录坑：在属性访问拦截器中不可以再使用self. 这类的语法

    def test(self):
        print("heihei")

p = Person()

p.a #返回haha

p.b #会让程序死掉，因为会递归调用__getattribute__
