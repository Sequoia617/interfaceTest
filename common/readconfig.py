# coding:utf-8
__author__ = 'lenovo'

import os
import codecs # 转编码用
import configparser # 读取配置文件模块

# 获取该文件的真实路径，然后分隔路径和文件名存入一个元组
# 获取路径方法一
proDir = os.path.split(os.path.realpath(__file__))[0]
# print(proDir)

# 获取路径方法二
# proDir = os.getcwd()
# print(proDir)

# 获取上层目录
parDir = os.path.dirname(proDir)
# print(parDir)
configPath = os.path.join(parDir,'config.ini')
# print('prodir:',proDir,configPath)

class ReadConfig(object):
    def __init__(self):
        # 1--实例化configparser对象
        self.cf = configparser.ConfigParser()
        # 2--调用read方法读取该文件（传参：文件路径和编码格式）
        self.cf.read(configPath)
        # self.cf.read(configPath,encoding="utf-8-sig")

    # 获取配置文件中的分组（eg:EMAIL）中的对应选项（eg:name）的值
    def get_email(self,name):
        # 3--获取某某section下的value，name相当于key
        value = self.cf.get('EMAIL',name)
        return value

    def get_http(self,name):
        value = self.cf.get('HTTP',name)
        return value

    def get_db(self,name):
        value = self.cf.get('DATABASE',name)
        return value

if __name__ == '__main__':
    p = ReadConfig()
    print(p.get_email('mail_user'))














