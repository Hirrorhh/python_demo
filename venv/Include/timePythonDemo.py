#!/usr/bin/env python

# encoding: utf-8

'''

@author: Hirror

@contact: hanhh@hefupb.com

@file: timePython.py

@time: 2018/3/26 10:01

@desc:和时间相关的python API

'''
import time;
import calendar;
print("当前时间: ",time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))

#按照一定格式显示时间
time_str = "%Y-%m-%d %H:%M:%S";
print("按照一定格式显示时间: " ,time.strftime(time_str, time.localtime()))

calDemo = calendar.month(2016,1)
print("2016年一月份日历: ")
print(calDemo)
