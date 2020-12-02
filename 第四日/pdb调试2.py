#coding=utf-8

'''

使用pdb调试的第二个demo

'''
import pdb

a = 'aaa'

pdb.set_trace()

b = 'bbb'
c = 'ccc'
pdb.set_trace()

final = a + b + c
print(final)
