# coding:utf-8
__author__ = 'lenovo'

# 1、找到excel对象
# 2、复制excel对象
# 3、写入

import xlrd
from xlutils.copy import copy  # 操作Excel文件的实用工具，如复制、分割、筛选等
import os

class writeExcel(object):

    dir = 'testData'
    current_dir = os.getcwd()+ "/" + dir
    print(current_dir)

    excel_dir = os.path.dirname(os.getcwd()) + '/' + dir
    # excel_dir = os.getcwd() + "/" + dir
    # print('excel_dir',excel_dir)

    # 1--读取源excel中的所有数据（复制对象）
    excel_path = excel_dir + '/' + 'data.xls'
    print(excel_path)
    rb = xlrd.open_workbook(excel_path)
    # rs = rb.sheet_by_index(2)
    # 2--复制读取的源excel对象
    wb = copy(rb)
    # 3--通过get_sheet()获取的sheet页（有write()方法）
    ws = wb.get_sheet(2)

    # def __str__(self):
    #     return '我在这里%s'%self.excel_dir

    def writeData(self,id,real,status):
        try:
            print('写入')

            # 根据id写入对应的实际结果和接口测试状态
            # 4--对sheet页进行写入(传入x,y和具体写入的value)
            self.ws.write(id,2,real)
            self.ws.write(id,3,status)

            # 5--保存excel(具体的excel路径+名称)
            self.wb.save(self.excel_dir + '/' + 'data.xls')
            return 'ok'
        except Exception as msg:
            print(msg)
if __name__ == '__main__':
    a = writeExcel
    print(a.writeData(0,0,'success'))
