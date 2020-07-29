# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/7/28 8:53
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
'''
从excel中读取多个数据，用于用例中，作为数据驱动
'''
from openpyxl import load_workbook

class Parse_Excel():
    def __init__(self,excel_path,sheetname):
        self.wb = load_workbook(excel_path)
        self.sheet = self.wb.get_sheet_by_name(sheetname)

    def getDataFromSheet(self):
        datalist = []

        for line in self.sheet.rows[1:]:
            tmplist= []
            tmplist.append(line[0].value)
            tmplist.append(line[1].value)
            datalist.append(tmplist)
        return datalist



if __name__ == '__main__':
    excel_path = './../data/baidu_test_data.xlsx'
    sheetname = 'baidu_sou'
    pe = Parse_Excel(excel_path,sheetname)
    print(pe.getDataFromSheet())
