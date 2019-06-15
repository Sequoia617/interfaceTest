# coding:utf-8
__author__ = 'lenovo'

# 1、加载目标测试用例
# 2、执行所有的用例，并把结果写入html报告
# 3、获取最新的测试报告
# 4、发送最新的测试报告

import unittest
import time
import os
import sys
import HTMLTestRunner
from common.readConfig import ReadConfig
from common.configEmail import configMyEmail
from testCase.TestCase import TestCase

class myTest(unittest.TestCase):

    def run_case(dir = "testCase"):
        # 按照指定目录加载目标用例
        case_dir = os.getcwd() + "/" + dir
        print(case_dir)
        discover = unittest.defaultTestLoader.discover(case_dir,pattern="TestCase*.py",top_level_dir=None)
        return discover

    def clear_report(self):
        nowPath = os.path.dirname(__file__)
        print('nowpath',nowPath)
        reportPath = nowPath + "/" + "report"
        fileList = os.listdir(reportPath)
        # 如果该目录下的文件超过5个，则开始清理
        if len(fileList)>5:
            for i in fileList:
                file = reportPath + "/" + i
                os.remove(file)

        fileNewList = os.listdir(reportPath)
        print(fileNewList)

if __name__ == '__main__':
    clear_report()
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path =os.getcwd() + "\\report\\" + current_time + '.html'  # 生成测试报告的路径
    print(report_path)
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"自动化测试报告", description=u'xx公司接口',verbosity=2)
    runner.run(run_case())
    fp.close()
    # c = ConfigEmail()
    # c.send_mail()