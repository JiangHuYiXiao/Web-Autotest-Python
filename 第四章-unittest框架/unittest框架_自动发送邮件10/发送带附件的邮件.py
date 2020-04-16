# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/16 9:05
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
import smtplib,datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
# d = datetime.date.today()
# strd = str(datetime.date.today())
# print('baidu'+str(datetime.date.today()))
# print(strd,type(strd))
# print(d,type(d))
def SendMailAttach():
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
    att = MIMEText(open('./result.html','rb').read(),'base64','utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename=result.html'
    msg.attach(att)
    mail_title = '百度搜索测试结果'+str(datetime.date.today())
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

SendMailAttach()