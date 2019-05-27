# coding:utf-8
__author__ = 'lenovo'

import requests
# from common import readConfig as readConfig

class ConfigHttp(object):
    # 定义get方法
    def get(self,url,param):
        print(url,param)
        response = requests.get(url,params=eval(param))
        result = response.text
        # 获取结果
        return result

