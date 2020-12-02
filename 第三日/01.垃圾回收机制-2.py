#coding=utf-8

'''
import gc
gc常用的函数
gc.get_count()当前会触发gc的引用计数
gc.get_threshold()获取的gc模块中自动执行垃圾回收的频率
gc.set_threshold(args1,args2,args3) 设置gc执行垃圾回收的频率




'''
import gc
import sys

gc.get_count()
gc.get_threshold()

a = "hello world"
sys.getrefcount(a)


