# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/14 8:05
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
# unittest框架是python的一个单元测试框架，不仅可以用于单元测试，也可以应用于web自动化测试
# 主要四个部分是：
    # 1、TestCase
    # # 2、TestSuite
    # # 3、TestFixture
    # # 4、TestRunner
# TestCase：用户自定义的测试case的基类，调用run()方法，会依次调用setUp方法、执行用例的方法、tearDown方法。

# TestSuite：测试用例集合，可以通过addTest()方法手动增加Test Case，也可以通过TestLoader自动添加Test Case，TestLoader在添加用例时，会没有顺序。

# TestRunner：运行测试用例的驱动类，可以执行TestCase，也可以执行TestSuite，执行后TestCase和TestSuite会自动管理TESTResult。

# TestFixture：简单来说就是做一些测试过程中需要准备的东西，比如创建临时的数据库，文件和目录等，其中setUp()和setDown()是最常用的方法

# 整个的流程就是首先要写好TestCase，然后由TestLoader加载TestCase到TestSuite，然后由TestTestRunner来运行TestSuite，运行的结果保存在TextTestReusult中，整个过程集成在unittest.main模块中。
