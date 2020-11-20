#coding=utf-8

'''

Python使用LEGB的顺序来查找一个符号对应的对象

L(locals)当前所在命名空间，函数的参数也属于命名空间的变量
E(enclosing)，外部嵌套函数的命名空间，闭包中常用
G(globals),全局变量
B(builtins)，内建变量 查看内建变量的方法dir(__builtins__)


'''
#num = 100定义全局变量
def Pnum(): # 定义一个闭包
   #num = 200 定义闭包的变量
    def Pnum2():
        #num = 300 定义内部变量
        print("num=%d"%num)
    return Pnum2

ret = Pnum()
ret()


