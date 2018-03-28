#!/usr/bin/env python

# encoding: utf-8

'''

@author: Hirror

@contact: hanhh@hefupb.com

@file: classPythonDemo.py

@time: 2018/3/27 10:10

@desc:

'''
class Student:
    empcount = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.empcount += 1


    def showName(self):
        print(self.name)

    def showAllNUm(self):
        print("show all student count %d " % Student.empcount)


student1 = Student("lacy", 18)
student2 = Student("jack", 28)

student1.showName()
student1.showAllNUm()

student2.showName()
student2.showAllNUm()
setattr(student2,"name","hirror")
student2.showName()



