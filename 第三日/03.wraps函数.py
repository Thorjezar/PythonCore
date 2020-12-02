#coding=utf-8

'''
wraps函数

'''
import functools

def note(func):
    "note function"
    @functools.wraps(func)
    def wrapper():
        "wrapper function"
        print("note something")
        return func
    return wrapper

@note
def test():
    "test function"
    print("I am test")


help(test())

