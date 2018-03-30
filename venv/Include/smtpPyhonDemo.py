#!/usr/bin/env python
#encoding: utf-8

"""

@author: Hirror

@contact: hanhh@hefupb.com

@file: smtpPyhonDemo.py

@time: 2018/3/30 16:08

@desc:

"""
import smtplib

from email.mime.text import MIMEText
from email.header import Header

mail_HostName="smtp.exmail.qq.com"
mail_SmtpPort=465
mail_UserName="sysinfo@hefupb.com"
mail_Password="Hfjf8888"
mail_SSLOnConnect="true"
mail_From="sysinfo@hefupb.com"
mail_charset="UTF-8"


receiver = ["hanhh@hefupb.com"]

message = MIMEText("测试python发送邮件ByHirror","plain","utf-8")
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


