# coding:utf-8
__author__ = 'lenovo'

import xlrd
from xlutils.copy import copy
import os

class writeExcel(object):
    dir = 'testData'
    # current_dir = os.getcwd()+ "\\" + dir
    # print(current_dir)
    excel_dir = os.path.dirname(os.getcwd())  + "\\" + dir
    print(excel_dir)
    excel_dir = os.getcwd()  + "\\" + dir
    print('excel_dir',excel_dir)

    rb = xlrd.open_workbook(excel_dir + '\\' + 'data.xls')
    rs = rb.sheet_by_index(2)
    # xlutils
    # xlrd只能读取xls，xlwt只能新建xls（不可以修改）
    # xlutils能将xlrd.Book转为xlwt.Workbook，从而得以在现有xls的基础上修改数据，并创建一个新的xls，实现修改
    wb = copy(rb)

    # 通过get_sheet()获取的sheet有write()方法
    ws = wb.get_sheet(2)
    def writeData(self,id,real,status):
        try:
            print('写入')
            #根据id写入对应的实际结果和接口测试状态
            self.ws.write(id,2,real)
            self.ws.write(id,3,status)
            self.wb.save(self.excel_dir + '\\' + 'data.xls')
            return 'ok'
        except Exception as msg:
            print(msg)