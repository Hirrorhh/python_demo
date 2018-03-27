#!/usr/bin/env python

# encoding: utf-8

'''

@author: Hirror

@contact: hanhh@hefupb.com

@file: filePythonDemo.py

@time: 2018/3/26 14:11

@desc:

'''
import codecs#解决写入中文时编码是GBK导致乱码
foDemo = codecs.open("test.txt","w","utf-8")
foDemo.write("三天以来共有数百位在京学子注册了西安户政的“掌上户籍室”，\n并有十数名硕士、博士生通过“掌上户籍室”现场办理完成落户西安\n")
foDemo.write("sfsdfsdfsf")
foDemo.close()
