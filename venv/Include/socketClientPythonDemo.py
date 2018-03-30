#!/usr/bin/env python

# encoding: utf-8

'''

@author: Hirror

@contact: hanhh@hefupb.com

@file: socketClientPythonDemo.py

@time: 2018/3/30 11:29

@desc:

'''
import socket

s = socket.socket()
hostName = socket.gethostname()
port = 1256
print(hostName)
s.connect((hostName, port))
print (s.recv(1024))
s.close()