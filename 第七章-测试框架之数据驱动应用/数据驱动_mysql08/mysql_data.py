# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/6/26 8:24
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
'''
提供mysql驱动的数据
'''
import pymysql
from mysql_init import MysqlInit

class MysqlData():
    def __init__(self,host,database,port,user,password,charset):
        self.host = host
        self.database = database
        self.port = port
        self.user = user
        self.password = password
        self.charset = charset
        MI = MysqlInit(
            host='localhost',
            database='db1',
            port=3306,
            user='root',
            password='123',
            charset='utf8')  # 创建数据库初始化对象
        MI.init_create_sql()
        MI.init_insert_sql()
        print('数据库初始化完成')

    def get_mysql_data(self):

        self.conn = pymysql.connect(host=self.host,
                                    database=self.database,
                                    port=self.port,
                                    user=self.user,
                                    password=self.password,
                                    charset=self.charset)
        self.conn.select_db('db1')
        self.cursor = self.conn.cursor()
        sql = "select testdata,exceptdata from t_jianghu_user;"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        print(data)
        return data

if __name__ =='__main__':
    mysql_data = MysqlData(
        host='localhost',
        database='db1',
        port=3306,
        user='root',
        password='123',
        charset='utf8')
    mysql_data.get_mysql_data()

