# coding:utf-8
__author__ = 'lenovo'

import xlrd
from xlutils.copy import copy
import os

class writeExcel(object):
    dir = 'testData'
    # current_dir = os.getcwd()+ "\\" + dir
    # print(current_dir)
    excel_dir = os.path.dirname(os.getcwd())  + '\\' + dir
    print(excel_dir)
    # excel_dir = os.getcwd() + "\\" +dir
    # print('excel_dir',excel_dir)
    # 1--读取源excel中的所有数据（复制对象）
    rb = xlrd.open_workbook(excel_dir + '\\' + 'data.xls')
    rs = rb.sheet_by_index(2)
    # 2--复制读取的源excel对象
    wb = copy(rb)
    # 3--通过get_sheet()获取的sheet页（有write()方法）
    ws = wb.get_sheet(2)

    def __str__(self):
        return ('---',os.path.dirname(os.getcwd()))

    def writeData(self,id,real,status):
        try:
            print('写入')
            # 根据id写入对应的实际结果和接口测试状态
            # 4--对sheet页进行写入(传入x,y，具体写入的value)
            self.ws.write(id,2,real)
            self.ws.write(id,3,status)
            # 5--保存excel(具体的excel路径+名称)
            self.wb.save(self.excel_dir + '\\' + 'data.xls')
            return 'ok'
        except Exception as msg:
            print(msg)

a = writeExcel
a.writeData()
