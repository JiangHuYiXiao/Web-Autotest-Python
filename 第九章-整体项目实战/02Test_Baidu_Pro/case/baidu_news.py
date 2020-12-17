# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/7/27 8:31
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
import time,unittest,logging,traceback,ddt
from selenium import webdriver
from baidu_tools import screen_shot
from selenium.common.exceptions import NoSuchElementException
from baidu_tools.ReadExcel import Parse_Excel
from baidu_tools.create_log import Log
excel_path = './../data/baidu_test_data.xlsx'
sheetname = 'news_sou'
excel = Parse_Excel(excel_path,sheetname)
now_time = time.strftime('%Y_%m_%d %H_%M_%S')    # 2020_01_01 12_14_05

@ddt.ddt
class Baidu_Search(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(6)
        self.driver.maximize_window()
        self.driver.get('http://news.baidu.com/')
        self.log = Log()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def setUp(self):
        pass

    @ddt.data(* excel.getDataFromSheet())
    def test_search(self,data):
        try:
            self.driver.find_element_by_xpath('//input[@id="ww"]').send_keys(data[0])
            time.sleep(2)
            self.driver.find_element_by_xpath('//input[@id="s_btn_wr"]').click()
            time.sleep(2)
            self.assertEqual(data[1]+'_百度搜索',self.driver.title)
        except NoSuchElementException as e:
            # logging.error("查找的页面元素不存在，异常堆栈信息：" + str(traceback.format_exc()))  # 抛出具体的代码异常的堆栈信息
            self.driver.get_screenshot_as_file('./../report/'+now_time[:10]+'/png/'+data[1]+'.png')
            self.log.addlog(data[0], data[1], format(e))
        except AssertionError as e:
            # logging.info("搜索:%s,期望:%s,失败" % (data[0], data[1]))
            self.driver.get_screenshot_as_file('./../report/'+now_time[:10]+'/png/'+data[1]+'.png')
            self.log.addlog(data[0], data[1], format(e))
        except Exception as e:
            # logging.error('未知错误，信息：' + str(traceback.format_exc()))
            self.driver.get_screenshot_as_file('./../report/'+now_time[:10]+'/png/'+data[1]+'.png')
            self.log.addlog(data[0], data[1], format(e))
        else:
            print('***************************')
            self.log.addlog(data[0], data[1], '用例执行通过')
            # logging.info("搜索:%s,期望:%s,通过" % (data[0], data[1]))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()


