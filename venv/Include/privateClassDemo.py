#!/usr/bin/env python

# encoding: utf-8

'''

@author: Hirror

@contact: hanhh@hefupb.com

@file: privateClassDemo.py

@time: 2018/3/27 14:07

@desc:

'''

class JustCounter:
    __secrect=0
    publicCount = 1

    def count(self):
        self.__secrect +=1
        self.publicCount +=1
        print(self.__secrect)

counter = JustCounter()
counter.count()
counter.count()
print (counter.publicCount)
#print (counter.__secretCount)  # 报错，实例不能访问私有变量
print(counter._JustCounter__secrect)