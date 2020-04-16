# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/15 19:27
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发送邮箱服务器
smtpserver = 'smtp.qq.com'

# 发送邮箱用户名/密码
user = '1721906562@qq.com'
password = 'wkqcqxwklgqmgeda'     # BFSUCWNDHFDRJOGY

# 发送邮箱
sender = '1721906562@qq.com'

# 接收邮箱
receiver = '1163270704@qq.com'    #

# 发送邮箱主题
subject = '百度搜索测试报告'

# 编写HTML类型的邮件正文
msg = MIMEText('正文内容')
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receiver

# 链接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())

smtp.quit()
