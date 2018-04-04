#!/usr/bin/env python
# encoding: utf-8

'''

@author: Hirror

@contact: hanhh@hefupb.com

@file: theadPythomDemo.py

@time: 2018/4/2 9:27

@desc:

'''
import thread
import time
time_str = "%Y-%m-%d %H:%M:%S";
def printTime(sleepTime, declareName):
    count = 0
    while count <5:
        time.sleep(sleepTime)
        count +=1
        print("%s: %s" % (declareName, time.strftime(time_str,time.localtime())))

try:
    thread.start_new_thread(printTime,(2,"thread1"))
    thread.start_new_thread(printTime,(5,"thread2"))
except:
    print("thread test err")

while 1:
    pass