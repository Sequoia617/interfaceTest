# coding:utf-8
__author__ = 'lenovo'

import requests
from common import readConfig as readConfig
localReadConfig = readConfig.ReadConfig

class ConfigHttp(object):
    # 创建get方法
    def get(self,url,param,cookie=None,header=None,timeout=3):

        try:  # try捕获异常
            # print(url,param)
            response = requests.get(url=url,params=eval(param),data=None,header=header,cookies=cookie,timeout=timeout)
            result = response.text
            # 获取结果
            return result
        except Exception as msg:
            print('request error,please check out!')
            return None

    # 创建post方法
    def post(self,url,param,cookie=None,header=None,timeout=3):
        try:
            # 如果post请求里有get参数，加上params='XXX'
            response = requests.post(url=url,data=eval(param),param=None,headers=header,cookies=cookie,timeout=timeout)
            result = response.text
            # print(result)
            return result
        except Exception as msg:
            print('request error,please check out!')
            return None

    # 创建一个getRequest方法根据传入参数判断请求的接口是get方法还是post方法
    def getRequest(self,url,method,param):
        if str(method) == 'get':
            return self.get(url,param)
        elif str(method) == 'post':
            return self.post(url,param)






