#!/usr/bin/env python
# encoding: utf-8

'''

@author: Hirror

@contact: hanhh@hefupb.com

@file: smtpAttachHtmlDemo.py

@time: 2018/3/30 16:59

@desc:

'''
import smtplib
from email.mime.multipart import MIMEMultipart
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
message = MIMEMultipart()
message["From"] = Header("hirror","utf-8")
message["To"] =Header("测试","utf-8")
message.attach(MIMEText(mail_msg,"html","utf-8"))
att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)

# 构造附件2，传送当前目录下的 runoob.txt 文件
att2 = MIMEText(open('demo.txt', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
message.attach(att2)

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

