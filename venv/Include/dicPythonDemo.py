#!/usr/bin/env python

# encoding: utf-8

'''

@author: Hirror

@contact: hanhh@hefupb.com

@file: dicPythonDemo.py

@time: 2018/3/26 9:26

@desc: python 类似于java中的map 键值唯一,多次重复键值保留后一位的值,value可以取python对象中的任意

键值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
'''
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
dictTest1 = {"Alice": "15555","lefth": "9856"}
print(dict['Alice'])
dict['Beth']=9999
print(dict['Beth'])

del dict['Cecil']
print(dict)
# dict.clear()
# print("清空之后的字典: ",dict)
# del dict
# print("删除之后的字典: ",dict)
print(dict.get('alice', "nothing"))
print ("Value : %s" %  dict.get('Sex', "Never"))
print(dict.items())
print("打印字典键值API: ",dict.keys())
dict.setdefault("firstDefault","first")
print("打印字典的值: ",dict.values())
dict.update(dictTest1)
print("dict按另一个字典更新 ",dict)