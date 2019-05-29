# coding:utf-8
__author__ = 'lenovo'

import requests
# from common import readConfig as readConfig


class ConfigHttp(object):
    # 定义get方法
    def get(self,url,param):
        try:
            print(url,param)
            response = requests.get(url,params=eval(param))
            result = response.text
            # 获取结果
            return result
        except Exception:
            print('request error,please check out!')
            return None
    # 定义post方法
    def post(self,url,param):
        try:
            response = requests.post(url,data=eval(param))
            result = response.text
            print(result)
            return result
        except Exception:
            print('request error,please check out!')
            return None
    # 判断请求的接口是get方法还是post方法
    def getRequest(self,url,method,param):
        if str(method) == 'get':
            return self.get(url,param)
        elif str(method) == 'post':
            return self.post(url,param)






