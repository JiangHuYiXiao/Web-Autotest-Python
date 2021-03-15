# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/3/8 8:32
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

from Project.企业微信.PageObject实战2.page.admin import Admin


class Test_Add_Member():
    def setup(self):
        self.admin = Admin()

    def test_add_member(self):
        assert(self.admin.goto_add_member().save_contacts())

