# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/2/9 15:44
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
'''
使用driver.get_cookies()获取当前页面的所有cookie
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Test_cookies():
    def setup(self):
        # chrome_options = Options()
        # chrome_options.debugger_address = '127.0.0.1:9666'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_cookies(self):
        # self.driver.get('https://work.weixin.qq.com/')
        '''
        expiry是一个有效期，expiry的value为小数的需要改成整数，否则会报错
        '''
        cookies = [{'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
                    'secure': False, 'value': '4721602228'},
                   {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/',
                    'secure': False, 'value': '6eeea3e5e11d0d3e6dfaaab6c3791bac3b21ec351fd8d8221138890407b83f12'},
                   {'domain': '.qq.com', 'expiry': 9178189959, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
                    'secure': False, 'value': '9b900d26e7c637d1'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/',
                    'secure': False, 'value': '1286243803387350'},
                   {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
                    'secure': False, 'value': '1963840512'},
                   {'domain': '.qq.com', 'expiry': 2147483652, 'httpOnly': False, 'name': 'RK', 'path': '/',
                    'secure': False, 'value': 'fmY1kPCSMr'},
                   {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
                    'secure': False, 'value': '1721906562'},
                   {'domain': '.work.weixin.qq.com', 'expiry': 1615450006, 'httpOnly': False,
                    'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'},
                   {'domain': '.qq.com', 'expiry': 1925282588, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
                    'secure': False, 'value': '1_1721906562'},
                   {'domain': '.work.weixin.qq.com', 'expiry': 1644283352, 'httpOnly': False,
                    'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/',
                    'secure': False, 'value': '1688851101646656'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/',
                    'secure': False, 'value': '1'},
                   {'domain': 'work.weixin.qq.com', 'expiry': 1612867272, 'httpOnly': True, 'name': 'ww_rtkey',
                    'path': '/', 'secure': False, 'value': '674qbjt'},
                   {'domain': '.work.weixin.qq.com', 'expiry': 1644391160, 'httpOnly': False,
                    'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                    'value': '1612747456,1612854185,1612855160'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/',
                    'secure': False, 'value': 'direct'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/',
                    'secure': False, 'value': 'a1262207'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/',
                    'secure': False, 'value': 'bxc6UTYFenvI83Ii-VUreB3_3FKZVovi37fFP6c2mp39DUUVQT5w1FAygtIi_d6_'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/',
                    'secure': False, 'value': '1970325135364316'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/',
                    'secure': False,
                    'value': 'YN50qQNrv0-Ke7mBqgUSdc16BZyF3EcO2aRStdTtDl519V8wbZLNrpjoXOL_qNN2mHX8fIH8zqKvNMKrHFfD9H-5tH6HaQe7VUOtfgw4FEG4MCp_IY4IFzEasqc-ZfSK1XpjZZT0fH1IJ1E3EeEWK19ckv9ymgcmCHtJUcoLmYqefYChB6jx0CnPpWStf46E1SkSD96o38TFU72_JR4cWa5fhQ_eOyE_gGIj43Bgea_Sn-2q6EM9aQF1dYSRlRSjuU4SoCRFdOKElFw5JY9vCw'},
                   {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/',
                    'secure': False, 'value': '1688851101646656'}]
        # print(self.driver.get_cookies())     # 第一步，首先通过get方法获取cookies

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')   # 第二步
        for cookie in cookies:
            self.driver.add_cookie(cookie)                                          # 第三步


        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')          # 第四步

    def teardown(self):
        self.driver.quit()
