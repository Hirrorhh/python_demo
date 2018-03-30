#!/usr/bin/env python

# encoding: utf-8

'''

@author: Hirror

@contact: hanhh@hefupb.com

@file: mysqlInsertDemo.py

@time: 2018/3/30 10:21

@desc:

'''
import MySQLdb


conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='sbtest', charset='utf8')

cursor = conn.cursor()

sql = "INSERT INTO `sbtest`.`user` (`id`, `username`, `psw`) VALUES ('%d', '%s', '%s')" % (6,'testuser2','123444')

try:
    cursor.execute(sql)
    conn.commit()
except:
    conn.rollback()

conn.close()