# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/5/6 9:27
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
# 使用importorskip装饰器需要有参数，表示跳过这整个模块的用例，放在哪个文件 哪个文件下的用例就会全部跳过

import pytest
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

@pytest.importorskip('laohu')

def test_baidu():
    driver.get('https://www.baidu.com/')
    sleep(2)
    assert(driver.title =='百度一下，你就知道')


def test_sohu():
    driver.get('https://www.sohu.com/')
    sleep(2)
    assert(driver.title =='搜狐')
    driver.quit()