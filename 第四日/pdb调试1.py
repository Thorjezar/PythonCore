#coding=utf-8

'''

使用pdb调试的第一个demo

'''
import pdb

a = 'aaa'

pdb.set_trace()

b = 'bbb'
c = 'ccc'

final = a + b + c
print(final)
