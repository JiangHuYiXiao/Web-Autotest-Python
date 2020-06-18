# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/6/17 8:48
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
import unittest,time,logging,ddt,traceback
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from Report_Template import htmlTemplate
from ExcelUtil import ParseExcel
# 1、初始化日志对象
logging.basicConfig(
    level=logging.INFO,
    # format='%(asctime)s %(filename)s(line:%[lineno]s)%(levelname)s%(level)s%(messgae)s',
    format='%(asctime)s %(filename)s[line:%(lineno)s] %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='./test_excel,log',
    filemode='w'

)
excelpath = 'F:/Web-Autotest-Python/第七章-测试框架之数据驱动应用/数据驱动_excel数据的读取操作06/excel测试数据.xlsx'
sheetname = '百度搜索'
excel = ParseExcel(excelpath,sheetname)

# 2、创建Excel类


@ddt.ddt                        # 声明ddt
class TestExcel(unittest.TestCase):
    '''excel测试类'''
    @classmethod
    def setUpClass(self):
        # 使用类去操作静态属性baidu
        TestExcel.baidu=''
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def setUp(self):
        self.driver.get('http://www.baidu.com/')
        self.driver.implicitly_wait(5)

    @ddt.data(* excel.getDatasFromSheet())                 # 加载数据,使用对象excel调用
    @ddt.unpack                 # 传递数据 data
    def test_excel(self,testdata,exceptdata):
        print(testdata)
        print(exceptdata)
        flagDict = {0:'red',1:'green'}
        try:
            start= time.time()          #时间戳时间
            start_time = time.strftime("%Y-%M-%d %H:%M:%S", time.localtime())                # 格式化时间
            self.driver.find_element_by_xpath("//input[@id='kw']").clear()
            self.driver.find_element_by_xpath('//input[@id="kw"]').send_keys(testdata)
            time.sleep(2)
            self.driver.find_element_by_xpath("//input[@id='su']").click()
            time.sleep(2)
            self.assertIn(exceptdata,self.driver.page_source,'用例执行不通过')
        except NoSuchElementException as e:
            logging.info('页面元素不存在，异常堆栈信息为：'+str(traceback.format_exc()))
            flag = 0
            status = 'fail'
        except AssertionError as e:
            logging.info('预期%s结果和实际%s结果不相符，用例执行不通过'%(testdata,exceptdata))
            flag = 0
            status = 'fail'
        except Exception as e:
            logging.error('未知错误，用例执行不通过'+str(traceback.format_exc()))
            flag = 0
            status = 'fail'
        else:
            logging.info('预期%s结果和实际%s结果相符，用例执行通过'%(testdata,exceptdata))
            flag = 1
            status = 'pass'
        wastetime =time.time()-start            # 记录耗时s
        TestExcel.baidu += '''
            <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%.2f</td>
            <td style="color:%s;">%s</td>
            </tr>''' % (testdata,exceptdata,start_time,wastetime,flagDict[flag],status)

    def tearDown(self):
        print(TestExcel.baidu)
    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        # 调用htmlTemplate测试模板
        htmlTemplate(TestExcel.baidu)


if __name__ == '__main__':
    unittest.main()


