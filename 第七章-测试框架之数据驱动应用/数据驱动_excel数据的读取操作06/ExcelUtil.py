# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/6/17 10:40
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7
from openpyxl import load_workbook

class ParseExcel():
    def __init__(self,excelpath,sheetname):
        self.wb = load_workbook(excelpath)
        self.sheet = self.wb.get_sheet_by_name(sheetname)

    def getDatasFromSheet(self):
        datalist= []

        for line in self.sheet.rows[1:]:            # 从第二行开始
            tmplist=[]
            tmplist.append(line[0].value)           # 每行的第一个单元格
            tmplist.append(line[1].value)           # 每行的第二个单元格
            datalist.append(tmplist)
        return datalist

if __name__ =='__main__':
    excelpath='F:/Web-Autotest-Python/第七章-测试框架之数据驱动应用/数据驱动_excel数据的读取操作06/excel测试数据.xlsx'
    sheetname = '百度搜索'
    pe= ParseExcel(excelpath,sheetname)
    print(pe.getDatasFromSheet())                   # [['Demon', 'Demon'], ['江湖', '江湖'], ['yixiu', 'yixiu']]
    for i in pe.getDatasFromSheet():
        print(i[0])