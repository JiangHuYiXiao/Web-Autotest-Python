# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/6/26 9:11
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
'''
使用ddt+unittest读取mysql数据
'''
import unittest, ddt
import pymysql
from mysql_data import MysqlData
from mysql_init import MysqlInit
def get_mysql_data():
    MD = MysqlData(
        host='localhost',
        database='db1',
        port=3306,
        user='root',
        password='123',
        charset='utf8')
    test_data = MD.get_mysql_data()
    return test_data

@ddt.ddt
class TestMysqlDdt(unittest.TestCase):

    @ddt.data( * get_mysql_data())          # 调用get_mysql_data函数
    @ddt.unpack
    def test_mysql(self, a, b):
        print(a, b)


if __name__ == '__main__':
    unittest.main()
