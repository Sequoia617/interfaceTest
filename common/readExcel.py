# coding:utf-8
__author__ = 'lenovo'

# 1.导入包
# 2.找到excel文件并打开(找不到文件时捕获异常)
# 3.定位sheet页
# 4.定位行和列
# 5.读取excel数据
# 6.组装测试数据，变为一条正确的匹配的接口测试数据
# 7.return data给testCase模块

# 1.导入包
import xlrd

class readExcel(object):
    # 找到excel文件并打开(找不到文件时捕获异常)
    # readbook = xlrd.open_workbook(r'F:\Code\interfaceTest\testDate\data.xls')
    readbook = xlrd.open_workbook(r'E:\VIPtest2\Code\interfaceTest\testDate\data.xls')
    # 获取所有的sheet页名字的列表
    sheetlist = readbook.sheet_names()
    # print(sheetlist)
    # 将读取的数据存入一个列表
    sheetUrl = []
    sheetParam = []
    sheetAssert = []
    # 获取sheet页数据
    def getData(self):
        # 定位sheet页
        for n in self.sheetlist:
            # print('sheet页的名称为：',n)
            # 通过名字区分每个sheet页的数据
            sheet = self.readbook.sheet_by_name(n)
            # 通过索引定位sheet页
            # sheet = self.readbook.sheet_by_index(0)
            # 定位行和列
            sheet_nrows = sheet.nrows # 获取sheet页最大行数
            sheet_ncols = sheet.ncols  # 获取sheet页最大列数
            # print(sheet_ncols,sheet_nrows)
            # 读取excel数据（循环读取excel表格）
            for i in range(1,sheet_nrows):
                row_values = sheet.row_values(i)
                if self.sheetlist.index(n) == 0:
                    self.sheetUrl.append(row_values)
                    # print(row_values)
                elif self.sheetlist.index(n) == 1:
                    self.sheetParam.append(row_values)
                elif self.sheetlist.index(n) == 2:
                    self.sheetAssert.append(row_values)
            # print(self.sheetUrl,self.sheetParam,self.sheetAssert)
        # 组装测试数据，将三个列表按照id进行匹配，变为一条正确的匹配的接口测试数据
    def assembleData(self):
        self.getData()  # 执行getData方法将数据取出来
        datalist = []
        for i in range(len(self.sheetUrl)):
            data = self.sheetUrl[i]+self.sheetParam[i][1:]+list(self.sheetAssert[i][1])
            # print(data)
            datalist.append(data)
        # print(datalist)
        return datalist

if __name__ == '__main__':
    p = readExcel()
    read = readExcel()
    read.getData()
    print(read.assembleData())



