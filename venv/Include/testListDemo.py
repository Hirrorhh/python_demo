#!/usr/bin/env python

# encoding: utf-8

'''

@author: Hirror

@contact: hanhh@hefupb.com

@file: testListDemo.py

@time: 2018/3/23 13:59

@desc:

'''

list01 = ("test01", "test02", "测试3")
list02 = ("testList01", "testList02", "testList04")
print(list01),
print(list02),
print(list01 + list02)
print(list02[1:2])
dic={"name":"hirror", "age":"18", "desc":"nice描述"}
dic1={};
dic1["first"]="firstValue"
dic1["one"]="oneValue"
print(dic.keys())
print(dic.values())
print(dic1.keys())
print(dic1.values())
# for str in list01:
#     print("依次遍历: ",str)
for str1 in dic:
    if str1 == "age":
        print("true")
        break
    print("依次遍历: ",str1)
