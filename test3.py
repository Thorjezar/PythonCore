# coding=utf-8

'''

生成器的第一种方法：
b = (x*2 for x in range(10))

        第二种方法：斐波拉契数列


'''
def creatNum():
    print("-----start------")
    a, b = 0, 1
    for i in range(5):
        print("------1------")
       #  print(b)
        yield b # 生成器的第二种方法      
        print("------2------")
        a, b = b, a+b
        print("------3------")
    
    print("-----stop------")

a = creatNum()

ret = a.__next__()
print(ret)


# 利用循环调用生成器
#for i in a:
 #   print(i)

#next(a)
# 等价于
#a.__next__()

