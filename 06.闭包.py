#coding = utf-8

'''

def test():
    print(1)

b = test
b() 可以直接调用函数，也就是说名称可以随意的更换

C++ JAVA等静态语言都没有这样的特性
在函数内部再定义一个函数，并且这个函数用到了外边函数的变量
将这个函数以及用到的外部变量统称为闭包

'''

def test(number):

    print("---1---")
    
    def test_in(number2):
        print("---2---")
        print(number+number2)

    print("---3---")
    return test_in


ret = test(100)
print("-"*30)
ret(1)
ret(100)
ret(200)



