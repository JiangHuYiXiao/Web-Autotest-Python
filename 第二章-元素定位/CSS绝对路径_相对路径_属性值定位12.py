# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/4/10 8:38
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://news.baidu.com')

# 绝对路径定位
# driver.find_element_by_css_selector('html.expanded>body>div#headerwrapper>div#header>table#sbox.sbox>tbody>tr>td.search>table>tbody>tr>td.box>div#sugarea>span#s_ipt_wr.s_ipt_wr>input#ww.word').send_keys('霸王别姬')
driver.find_element_by_css_selector('input[name="word"]').send_keys('霸王别姬')

# 相对路径定位
# driver.find_element_by_css_selector('#s_btn_wr').click()

# 属性值定位
driver.find_element_by_css_selector('input[value="百度一下"]').click()


sleep(2)
driver.quit()