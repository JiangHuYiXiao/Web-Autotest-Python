# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/14 16:32
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
# 之前我们通过套件可以添加需要执行的用例，但是如果我们有很多用例去执行？那么我们如果也是一条条去addTest那就太麻烦了
# 方法1：
    # 针对多用例执行我们可以使用for循环把TestCase的用例放在一个列表中，然后循环去执行，显然这个方法也不太好用

# 方法2：
    # 通过discover来批量执行
    # 将所有的用例放到case中
import unittest
dir ='./case/'
print(dir)
suite = unittest.defaultTestLoader.discover(start_dir=dir,pattern='Test*.py')

if __name__ =="__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)