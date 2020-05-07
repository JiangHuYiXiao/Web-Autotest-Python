# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/5/7 8:10
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

'''
我们都知道在unittest框架中，有setup，teardown，setUpClass,tearDownClass这样的前置套件。
在pytest中不止有这四个套件：
    setup_module                    # 模块级别开始，开始于模块始末，全局的，只运行一次
    teardown_module                 # 模块级别结束
    setup_function                  # 模块中函数级别开始
    teardown_function               # 模块中函数级别结束
    setup_class                     # 类级别开始，只在类中前后运行一次(在类中)
    teardown_class                  # 类级别结束，只在类中前后运行一次(在类中)
    setup_method                    # 类中方法级别开始
    teardown_method                 # 类中方法级别结束
    setup
    teardown
'''

import pytest
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(6)
driver.maximize_window()

# 示例module，function：


# 示例class，method
class Test_Class():
    '''百度搜索类'''
    def setup_class(self):
        print('类开始')

    def teardown_class(self):
        print('类结束')
        driver.quit()
    def setup_method(self):
        print('类级别方法开始')
        driver.get('https://www.baidu.com/')
        sleep(2)

    def teardown_method(self):
        print('类级别方法结束')

    def setup(self):
        print('setup开始')

    def teardown(self):
        print('teardown结束')

    def test_baidu03(self):
        '''百度搜索一休用例'''
        driver.find_element_by_xpath('//input[@id="kw"]').send_keys('一休')
        sleep(2)
        driver.find_element_by_xpath('//input[@id="su"]').click()
        sleep(2)
        assert(driver.title == '一休_百度搜索')

    def test_baidu04(self):
        '''百度搜索江湖用例'''
        driver.find_element_by_xpath('//input[@id="kw"]').clear()
        driver.find_element_by_xpath('//input[@id="kw"]').send_keys('江湖')
        sleep(2)
        driver.find_element_by_xpath('//input[@id="su"]').click()
        sleep(2)
        assert(driver.title == '江湖_百度搜索')


def setup_module():
    print('模块开始')
    driver.get('https://www.baidu.com/')
    sleep(2)

def teardown_module():
    print('模块结束')
    driver.quit()

def setup_function():
    print('模块中函数开始')

def teardown_function():
    print('模块中函数结束')

def setup():
    print('setup开始')
def teardown():
    print('teardown结束')

def test_baidu01():
    '''百度搜索一休用例'''
    driver.find_element_by_xpath('//input[@id="kw"]').send_keys('一休')
    sleep(2)
    driver.find_element_by_xpath('//input[@id="su"]').click()
    sleep(2)
    assert(driver.title == '一休_百度搜索')

def test_baidu02():
    '''百度搜索江湖用例'''
    driver.find_element_by_xpath('//input[@id="kw"]').clear()
    driver.find_element_by_xpath('//input[@id="kw"]').send_keys('江湖')
    sleep(2)
    driver.find_element_by_xpath('//input[@id="su"]').click()
    sleep(2)
    assert(driver.title == '江湖_百度搜索')

if __name__=='__main__':
    pytest.main()

'''
est_pytest_fixture.py 模块开始
模块中函数开始
setup开始
.teardown结束
模块中函数结束
模块中函数开始
setup开始
.teardown结束
模块中函数结束
类开始
类级别方法开始
setup开始
.teardown结束
类级别方法结束
类级别方法开始
setup开始
.teardown结束
类级别方法结束
类结束
模块结束
                                              [100%]

============================= 4 passed in 35.25s ==============================
Process finished with exit code 0
'''
# 根据上面的结果我们可以很清晰的得到了pytest的用例运行优先级：
# setup_module>setup_function（setup_class）>setup_method>setup>test_用例>teardown> teardown_method>teardown_function(teardown_class)
# 其中setup_function和setup_class,哪个在前面就先运行哪个 ，根据代码运行从上到下
