# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/6/22 9:54
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
'''数据库初始化：
    1、连接数据库
    2、创建表
    3、插入表数据
    4、判断数据库初始化是否完成'''
import pymysql,traceback
from mysql_create import MysqlCreate


class MysqlInit():
    def __init__(self, host, database, port, user, password, charset):
        self.host = host
        self.database = database
        self.port = port
        self.user = user
        self.password = password
        self.charset = charset

    def init_create_sql(self):
        try:
            self.conn = pymysql.connect(host=self.host,
                                        database=self.database,
                                        port=self.port,
                                        user=self.user,
                                        password=self.password,
                                        charset=self.charset)
            self.conn.select_db('db1')          # 选择数据库
            self.cursor = self.conn.cursor()        # 创建游标用于执行sql语句
            self.cursor.execute(MysqlCreate.drop_sql)
            self.cursor.execute(MysqlCreate.create_sql)



        except Exception as e:
            print('数据库表创建失败，存在问题的堆栈为：'+traceback.format_exc())
        else:
            self.cursor.close()            # 关闭cursor操作
            self.conn.commit()            # 关闭cursor执行sql的操作
            self.conn.close()               # 关闭连接
            print('数据库表创建成功')

    def init_insert_sql(self):
        try:
            self.conn = pymysql.connect(host=self.host,
                                        database=self.database,
                                        port=self.port,
                                        user=self.user,
                                        password=self.password,
                                        charset=self.charset)
            self.conn.select_db('db1')          # 选择数据库
            self.cursor = self.conn.cursor()        # 创建游标用于执行sql语句
            self.cursor.execute(MysqlCreate.insert_sql)
        except Exception as e:
            print('表数据插入失败,存在问题的堆栈为：'+traceback.format_exc())

        else:
            self.cursor.close()            # 关闭cursor操作
            self.conn.commit()            # 关闭cursor执行sql的操作
            self.conn.close()               # 关闭连接
            print('表数据插入成功')



if __name__ == '__main__':
    MI = MysqlInit(
        host='localhost',
        database='db1',
        port=3306,
        user='root',
        password='123',
        charset='utf8')   # 创建数据库初始化对象
    MI.init_create_sql()
    MI.init_insert_sql()
    print('数据库初始化完成')



