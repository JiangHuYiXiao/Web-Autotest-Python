# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/3/8 8:29
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Project.企业微信.PageObject实战2.page.add_member import Add_Member

class Admin():
    def __init__(self):
        chrome_option = Options()
        chrome_option.debugger_address = '127.0.0.1:9222'
        self._driver = webdriver.Chrome(options=chrome_option)
        # self._driver.maximize_window()
        self._driver.get('https://work.weixin.qq.com/wework_admin/frame')


    def goto_add_member(self):
        '''
        首页直接点击添加成员，跳转到添加成员列表页面
        :return:Add_Member()
        '''
        # sleep(3)
        # self._driver.find_element_by_css_selector('.index_service_cnt_itemWrap:nth-child(1)').click()
        # return Add_Member(self._driver)

        '''
        如果首页的添加成员不能用了，我们就可以直接在通讯录进行添加成员，这个时候就提现了PO的价值，不需要改很多内容只需要修改PO
        在通讯录点击添加成员
        '''
        sleep(3)
        self._driver.find_element_by_css_selector('#menu_contacts').click()
        sleep(10)
        self._driver.find_element_by_css_selector('.js_has_member>div.ww_operationBar:nth-child(1)>a:nth-child(2)').click()
        return  Add_Member(self._driver)



    def goto_import_member(self):
        pass

