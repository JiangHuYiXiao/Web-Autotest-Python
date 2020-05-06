# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/5/6 9:13
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
import pytest
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
@pytest.mark.xfail                  # 标记为失败，假失败，用例会执行
def test_baidu():
    driver.get('https://www.baidu.com/')
    sleep(2)
    assert(driver.title =='百度一下，你就知道')


def test_sohu():
    driver.get('https://www.sohu.com/')
    sleep(2)
    assert(driver.title =='搜狐')
    driver.quit()