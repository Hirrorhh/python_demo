#!/usr/bin/env python
# encoding: utf-8

'''

@author: Hirror

@contact: hanhh@hefupb.com

@file: smtpHtmlPythonDemo.py

@time: 2018/3/30 16:43

@desc:

'''
import smtplib

from email.mime.text import MIMEText
from email.header import Header

mail_HostName="smtp.exmail.qq.com"
mail_UserName="sysinfo@hefupb.com"
mail_Password="Hfjf8888"
mail_From="sysinfo@hefupb.com"



receiver = ["hanhh@hefupb.com"]

mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.hefupb.com">这是一个链接</a></p>
"""
message = MIMEText(mail_msg,"html","utf-8")
message["From"] = Header("hirror","utf-8")
message["To"] =Header("测试","utf-8")

subject = "Python SMTP 测试邮件发送"

message["Subject"] = Header(subject,"utf-8")
print("message",message)
print(message)
try:
    smtpO = smtplib.SMTP()
    smtpO.connect(mail_HostName,25)
    smtpO.login(mail_UserName,mail_Password)
    smtpO.sendmail(mail_From,receiver,message.as_string())
    print("发送邮件成功")

except:
    print("发送邮件出现错误...")

