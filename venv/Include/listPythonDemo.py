#!/usr/bin/env python

# encoding: utf-8

'''

@author: Hirror

@contact: hanhh@hefupb.com

@file: listPythonDemo.py

@time: 2018/3/23 17:09

@desc:

'''
import operator
list1 = ['Hirror', 'test', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

list4 = []
list4.append("测试")
list4.append("shili")
print("list1[0}",list1[0])
print("list2[1}",list2[1])
print("list3[2}",list3[2])
print("list4[0}",list4)

print("list[-2]",list1[-2])

print(operator.eq(list1,list2))