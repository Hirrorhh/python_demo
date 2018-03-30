#!/usr/bin/env python

# encoding: utf-8

'''

@author: Hirror

@contact: hanhh@hefupb.com

@file: socketPythonDemo.py

@time: 2018/3/30 11:23

@desc:

'''
import socket

s = socket.socket()
hostName = socket.gethostname()
port = 1256
print(hostName)
s.bind((hostName,port))
s.listen(5)
while True:
    c,address = s.accept();
    print("链接地址: ",address)
    c.send("我是server")
    c.close()