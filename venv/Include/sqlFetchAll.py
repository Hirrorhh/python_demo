#!/usr/bin/env python

# encoding: utf-8

'''

@author: Hirror

@contact: hanhh@hefupb.com

@file: sqlFetchAll.py

@time: 2018/3/30 10:31

@desc:

'''
import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='sbtest', charset='utf8')

cursor = conn.cursor()
#查询ID>2的数据
sql = "select * from USER WHERE  ID > '%d'" % (2)

try:
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        id = row[0]
        name = row[1]
        pwd = row[2]
        print("id: %d, name: %s, pwd : %s" % (id, name, pwd))

except:
    print("Error: fetch error")
    conn.rollback()

finally:
    conn.close()
