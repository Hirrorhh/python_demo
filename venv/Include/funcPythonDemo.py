#!/usr/bin/env python

# encoding: utf-8

'''

@author: Hirror

@contact: hanhh@hefupb.com

@file: funcPythonDemo.py

@time: 2018/3/26 10:59

@desc:

'''

#在python 中，类型属于对象，变量是没有类型的
def printDemo(printStr):
    "自定义函数demo,打印字符串"
    print(printStr)
    return


def ChangeInt(a):
    a = 10
    return a


print(ChangeInt(15))

printDemo("打印字符串...")

testFun = lambda num1,num2 : num1 + num2;

print(testFun(12, 34))
