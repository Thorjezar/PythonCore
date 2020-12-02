from threading import Thread
from time import sleep

def work1(nums):
    nums.append(44)
    print("---in work1---",nums)

def work2(nums):
    #sleep(1)
    print("---in work2---",nums)

g_num = [11, 22, 33]

if __name__=="__main__":
    t1 = Thread(target=work1, args=(g_num, ))
    t1.start()

    t2 = Thread(target=work2, args=(g_num, ))
    t2.start()
