# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/15 19:10
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
'''
整合发送普通邮件的程序和发送带有附件的邮件，以后直接在项目中使用
'''

import smtplib,datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def SendMail():
    # 发送邮箱服务器
    smtpserver = 'smtp.qq.com'

    # 发送邮箱用户名/密码
    user = '1721906562@qq.com'
    password = 'wkqcqxwklgqmgeda'  # BFSUCWNDHFDRJOGY

    # 发送邮箱
    sender = '1721906562@qq.com'

    # 接收邮箱
    receiver = '1163270704@qq.com'  #

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
# 调用发送邮件的方法
# SendMail()

def SendMailAttach(filename):
# 发送邮箱服务器
    smtpserver = 'smtp.qq.com'

    # 发送邮箱用户名/密码
    user = '1721906562@qq.com'
    password = 'wkqcqxwklgqmgeda'

    # 发送邮箱
    sender = '1721906562@qq.com'

    # 接收邮箱
    receiver = '1163270704@qq.com'    #

    # 编写HTML类型的邮件正文
    msg = MIMEMultipart()
    att = MIMEText(open(filename,'rb').read(),'base64','utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="'+filename[14:]+'"'     #附件的名称
    msg.attach(att)
    mail_title = '禅道测试结果'+str(datetime.date.today())
    msg['Subject'] = Header(mail_title, 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver

    body = 'Python Auto Test'
    msg.attach(MIMEText(body,'plain'))

    # 链接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)

    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())

    smtp.quit()
# 调用发送附件的邮件方法
# SendMailAttach()