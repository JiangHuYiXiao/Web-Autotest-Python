# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/6/8 9:06
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
'''
各参数信息：
filename: 指定日志文件名  
filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'  
format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:  
 %(levelno)s: 打印日志级别的数值  
 %(levelname)s: 打印日志级别名称  
 %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]  
 %(filename)s: 打印当前执行程序名  
 %(funcName)s: 打印日志的当前函数

 %(lineno)d: 打印日志的当前行号  
 %(asctime)s: 打印日志的时间  
 %(thread)d: 打印线程ID  
 %(threadName)s: 打印线程名称  
 %(process)d: 打印进程ID  
 %(message)s: 打印日志信息  
datefmt: 指定时间格式，同time.strftime()  
level: 设置日志级别，默认为logging.WARNING 
'''
# 分析：
    # 测试逻辑(WebDriver实例)
    # 打开百度首页
    # 在搜索框输入一个搜索关键词
    # 单击搜索按钮
    # 验证搜索结果页面是否包含预期关键字，如是则通过，否则判定失败，并在测试过程中打印日志。

from selenium import webdriver
import time,logging,ddt,unittest,traceback
from selenium.common.exceptions import NoSuchElementException
# 初始化日志对象
logging.basicConfig(
    level=logging.INFO,                                     # 日志级别
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',           # 日志格式
    datefmt='%a, %d %b %Y %H:%M:%S',                # 打印日志的时间
    filename='./report.log',                  # 日志文件存放的目录(目录必须存在)及日志文件名
    filemode='w'                                    # 打开日志文件的方式

)
# 声明ddt
@ddt.ddt
class Test_logging(unittest.TestCase):
    '''logging模块应用'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()
    @ddt.data(['江湖','江湖1'],['jianghu','jianghu'],['demon','demon'])                  # 添加数据
    @ddt.unpack                                            # 传递数据
    def test_baidu(self,testdata,exceptdata):
        try:
            self.driver.get('http://www.baidu.com/')
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_xpath('//input[@id="kw"]').send_keys(testdata)
            time.sleep(2)
            self.driver.find_element_by_xpath('//input[@id="su"]').click()
            time.sleep(2)
            self.assertIn(exceptdata,self.driver.page_source,'用例不通过')
        except NoSuchElementException as e:
            logging.error("查找的页面元素不存在，异常堆栈信息："+str(traceback.format_exc()))         # 抛出具体的代码异常的堆栈信息
        except AssertionError as e:
            logging.info("搜索:%s,期望:%s,失败" %(testdata,exceptdata,))
        except Exception as e:
            logging.error('未知错误，信息：'+str(traceback.format_exc()))
        else:
            logging.info("搜索:%s,期望:%s,通过" %(testdata,exceptdata,)
)

if __name__ == '__main__':
    unittest.main()

