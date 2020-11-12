# coding=utf-8

'''

生成器的第一种方法：
b = (x*2 for x in range(10))

        第二种方法：斐波拉契数列


'''
def creatNum():
    a, b = 0, 1
    for i in range(5):
        print("------1------")
       #  print(b)
        yield b # 生成器的第二种方法      
        print("------2------")
        a, b = b, a+b
        print("------3------")
