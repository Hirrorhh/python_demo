
#!/usr/bin/env python

# encoding: utf-8

'''

@author: Hirror

@contact: hanhh@hefupb.com

@file: mysqlPythonDemo.py

@time: 2018/3/29 17:25

@desc:

pip 安装pymysql模块: https://blog.csdn.net/qq_37176126/article/details/72824106
未安装pip的: https://blog.csdn.net/qq_37176126/article/details/72824404
'''
import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='sbtest', charset='utf8')
# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from user")

# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update tb7 set pass = '123' where nid = %s", (11,))

# 执行SQL，并返回受影响行数,执行多次
# effect_row = cursor.executemany("insert into tb7(user,pass,licnese)values(%s,%s,%s)", [("u1","u1pass","11111"),("u2","u2pass","22222")])

# 获取剩余结果的第一行数据
# row_1 = cursor.fetchone()
# print (row_1)

# 获取剩余结果前n行数据
# row_2 = cursor.fetchmany(3)
# print(row_2)


# 获取剩余结果所有数据
row_3 = cursor.fetchall()
print(row_3)

# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()