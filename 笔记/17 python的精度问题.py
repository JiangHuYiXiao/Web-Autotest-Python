# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/12/18 16:00
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
# >>> 0.1 +0.2
# 0.30000000000000004

from decimal import Decimal

result = Decimal('0.1') + Decimal('0.2')
print(result)