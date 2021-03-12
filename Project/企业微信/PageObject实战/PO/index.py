# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/2/26 16:29
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from selenium import webdriver
import time
from Project.企业微信.PageObject实战1.PO.Login_PO import Login
from Project.企业微信.PageObject实战1.PO.Register_PO import Register


class Index():
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.maximize_window()
        self._driver.get('https://work.weixin.qq.com/')

    # 点击登录按钮
    def click_login(self):
        self._driver.find_element_by_css_selector('.index_top_operation_loginBtn').click()
        return Login(self._driver)

    # 点击注册按钮
    def click_register(self):
        self._driver.find_element_by_css_selector('.index_head_info_pCDownloadBtn').click()
        time.sleep(4)
        return Register(self._driver)
