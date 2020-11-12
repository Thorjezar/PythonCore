#coding=utf-8

'''
元类就是用来创建类的“东西”。
元类就是类的类
Myclass = type('Myclass',(),{})


这是因为函数type实际上是一个元类。type就是Python在背后用来创建所有类的元类。现在你想知道那为什么type会全部采用小写形式而不是Type呢？好吧，我猜这是为了和str保持一致性，str是用来创建字符串对象的类，而int是用来创建整数对象的类。type就是创建类对象的类。你可以通过检查__class__属性来看到这一点。Python中所有的东西，注意，我是指所有的东西——都是对象。这包括整数、字符串、函数以及类。它们全部都是对象，而且它们都是从一个类创建而来，这个类就是type

因此，元类就是创建类这种对象的东西。type就是Python的内建元类，当然了，你也可以创建自己的元类。


__metaclass__属性

class Foo(object):
        __metaclass__ = something…
            ...省略...


如果你这么做了，Python就会用元类来创建类Foo。小心点，这里面有些技巧。你首先写下class Foo(object)，但是类Foo还没有在内存中创建。Python会在类的定义中寻找__metaclass__属性，如果找到了，Python就会用它来创建类Foo，如果没有找到，就会用内建的type来创建这个类。把下面这段话反复读几次。当你写如下代码时 :

    class Foo(Bar):
        pass

Python做了如下的操作：

Foo中有__metaclass__这个属性吗？如果是，Python会通过__metaclass__创建一个名字为Foo的类(对象)
如果Python没有找到__metaclass__，它会继续在Bar（父类）中寻找__metaclass__属性，并尝试做和前面同样的操作。
如果Python在任何父类中都找不到__metaclass__，它就会在模块层次中去寻找__metaclass__，并尝试做同样的操作。
如果还是找不到__metaclass__,Python就会用内置的type来创建这个类对象。
现在的问题就是，你可以在__metaclass__中放置些什么代码呢？答案就是：可以创建一个类的东西。那么什么可以用来创建一个类呢？type，或者任何使用到type或者子类化type的东东都可以。

现在回到我们的大主题上来，究竟是为什么你会去使用这样一种容易出错且晦涩的特性？好吧，一般来说，你根本就用不上它：

“元类就是深度的魔法，99%的用户应该根本不必为此操心。如果你想搞清楚究竟是否需要用到元类，那么你就不需要它。那些实际用到元类的人都非常清楚地知道他们需要做什么，而且根本不需要解释为什么要用元类。” —— Python界的领袖 Tim Peters
'''

class UpperAttrMetaClass(type):
    # __new__ 是在 __init__之前就被调用的特殊方法，是实例化类的方法
    # __new__是用来创建对象并返回的方法
    # 而__init__只是用来将传入的参数进行初始化
    # 这里创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
    def __new__(cls, future_class_name, future_class_parents, future_class_attr):
        # 遍历属性字典，把不是__开头的属性名字变为大写
        newAttr = {}
        for name,value in future_class_attr.items():
            if not name.startswith("__"):
                newAttr[name.upper()] = value

        # 方法1:通过'type'来做类对象的创建
        # return type(future_class_name, future_class_parents, newAttr)

        # 方法2:复用type.__new__方法
        # 这就是基本的OOP编程，没什么魔法
        # return type.__new__(cls, future_class_name, future_class_parents, future_class_attr)

        #方法3:使用super方法
        return super(UpperAttrMetaClass, cls).__new__(cls, future_class_name, future_class_parents,newAttr)
        

class Foo(object, metaclass = UpperAttrMetaClass):
    bar = 'bip'

print(hasattr(Foo, 'bar'))

print(hasattr(Foo, 'BAR'))

f = Foo()
print(f.BAR)


