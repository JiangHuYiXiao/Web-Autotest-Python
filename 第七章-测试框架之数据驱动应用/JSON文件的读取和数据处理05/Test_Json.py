# -*- coding:utf-8 -*-

# json在线格式化工具：
# https://www.bejson.com/

# 使用json数据文件来进行驱动
from selenium import webdriver
import time,unittest,ddt,logging,traceback
from Report_Template import htmlTemplate    # JSON文件的读取和数据处理05
from selenium.common.exceptions import NoSuchElementException
# 初始化日志对象
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(filename)s[line:%(lineno)s] %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='./test_json_log.log',
    filemode='w'
)


# 1、使用全局变量
'''
@ddt.ddt            # 声明
class Test1(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # 使用全局变量来解决，table表格数据为空的问题
        global baidu_test
        baidu_test = ' '
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    @classmethod
    def tearDownClass(self):
        # global baidu_test
        print(122121)
        self.driver.quit()
        htmlTemplate(baidu_test)

    def setUp(self):
        self.driver.get('http://www.baidu.com')

    def tearDown(self):
        # global baidu_test
        print(baidu_test)

    @ddt.file_data('data.json')                 # 加载json文件
    @ddt.unpack
    def test_baidu(self,value):
        flagDict = {0:'red',1:'green'}
        try:
            start = time.time()
            startTime = time.strftime(" %Y - %M - %d %H:%M:%S", time.localtime())
            testdata,exceptdata = value.split('||')
            print(testdata,exceptdata)
            self.driver.find_element_by_xpath('//input[@id="kw"]').clear()
            self.driver.find_element_by_xpath('//input[@id="kw"]').send_keys(testdata)
            time.sleep(2)
            self.driver.find_element_by_xpath('//input[@id="su"]').click()
            time.sleep(2)
            self.assertIn(exceptdata,self.driver.page_source,'用例执行不通过')
        except NoSuchElementException as e:
            logging.error("查找的页面元素不存在，异常堆栈信息：" + str(traceback.format_exc()))  # 抛出具体的代码异常的堆栈信息
            status = 'fail'
            flag = 0
        except AssertionError as e:
            logging.info("搜索:%s,期望:%s,失败" % (testdata,exceptdata))
            status = 'fail'
            flag = 0
        except Exception as e:
            logging.error('未知错误，信息：' + str(traceback.format_exc()))
            status = 'fail'
            flag = 0
        else:
            logging.info("搜索:%s,期望:%s,通过" % (testdata, exceptdata))
            status = 'pass'
            flag = 1
        wasteTime = time.time()- start
        # 使用全局变量来解决，table表格数据为空的问题
        global baidu_test
        baidu_test +='''
            # <tr>
            # <td>%s</td>
            # <td>%s</td>
            # <td>%s</td>
            # <td>%.2f</td>
            # <td style="color:%s;">%s</td>
            # </tr>''' % (testdata,exceptdata,startTime,wasteTime,flagDict[flag],status)


# 2、使用类的属性的方式解决table为空
@ddt.ddt            # 声明
class Test1(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # 使用类去操作静态属性

        Test1.baidu_test = ' '
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        htmlTemplate(Test1.baidu_test)

    def setUp(self):
        self.driver.get('http://www.baidu.com')

    def tearDown(self):
        # global baidu_test
        print(Test1.baidu_test)

    @ddt.file_data('data.json')                 # 加载json文件
    @ddt.unpack
    def test_baidu(self,value):
        flagDict = {0:'red',1:'green'}
        try:
            start = time.time()
            startTime = time.strftime(" %Y - %M - %d %H:%M:%S", time.localtime())
            testdata,exceptdata = value.split('||')
            print(testdata,exceptdata)
            self.driver.find_element_by_xpath('//input[@id="kw"]').clear()
            self.driver.find_element_by_xpath('//input[@id="kw"]').send_keys(testdata)
            time.sleep(2)
            self.driver.find_element_by_xpath('//input[@id="su"]').click()
            time.sleep(2)
            self.assertIn(exceptdata,self.driver.page_source,'用例执行不通过')
        except NoSuchElementException as e:
            logging.error("查找的页面元素不存在，异常堆栈信息：" + str(traceback.format_exc()))  # 抛出具体的代码异常的堆栈信息
            status = 'fail'
            flag = 0
        except AssertionError as e:
            logging.error("搜索:%s,期望:%s,失败" % (testdata,exceptdata))
            status = 'fail'
            flag = 0
        except Exception as e:
            logging.error('未知错误，信息：' + str(traceback.format_exc()))
            status = 'fail'
            flag = 0
        else:
            logging.info("搜索:%s,期望:%s,通过" % (testdata, exceptdata))
            status = 'pass'
            flag = 1
        wasteTime = time.time()- start
        # 使用全局变量来解决，table表格数据为空的问题

        Test1.baidu_test +='''
            <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%.2f</td>
            <td style="color:%s;">%s</td>
            </tr>''' % (testdata,exceptdata,startTime,wasteTime,flagDict[flag],status)

if __name__ == '__main__':
    unittest.main()
