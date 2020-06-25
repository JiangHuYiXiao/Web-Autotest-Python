# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/6/22 9:55
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
'''
本文件主要是创建表和插入表的sql语句，提供数据给后面的文件进行操作
'''
class MysqlCreate():
    drop_sql='''
        drop table if exists t_jianghu_user;
    '''

    create_sql='''
        
        create table if not exists t_jianghu_user(
        id int auto_increment PRIMARY KEY,
        testdata varchar (30)CHARACTER SET utf8 COLLATE utf8_general_ci,
        exceptdata varchar (30)CHARACTER SET utf8 COLLATE utf8_general_ci,
        result char (4))CHARACTER SET utf8 COLLATE utf8_general_ci;'''

    insert_sql ='''
    insert into t_jianghu_user(id,testdata,exceptdata) values
    (1,'Demon','Demon'),
    (2,'江湖','江湖'),
    (3,'laohu','laohu');'''


