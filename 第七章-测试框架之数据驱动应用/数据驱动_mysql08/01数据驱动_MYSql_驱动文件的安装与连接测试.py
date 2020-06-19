# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/6/18 19:33
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
import pymysql
conn = pymysql.connect(host='localhost',port=3306,user='root',password='123',database='db1',charset='utf8')
conn.select_db('db1')
cursor = conn.cursor()
sql = "select * from t_student"
cursor.execute(sql)
# 获取一个结果
res = cursor.fetchone()
if res:
    print('登录成功')
else:
    print('登录失败')
print(res,)
cursor.close()
conn.close()
