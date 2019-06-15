# coding:utf-8
__author__ = 'annie'

# 步骤
# 1、调用read_excel模块拿到测试数据
# 2、根据接口的请求方式判断调用XX方法
# 3、校验
# 4、保存执行结果
# 5、写入excel

import requests
# import json

from common.readExcel import readExcel

# 第一步
d = readExcel()
data = d.assembleData()
# print(data)

# 第二步
for i in data:
    # print(i[3])
    method = i[3]
    urlstr = i[1]
    param = eval(i[4])
    expect = int(i[-1])
    # url = i[1]

    if method == 'post':
        result = requests.post(url=urlstr,data=param)
        print(result.text)

    elif method == 'get':
        print(urlstr,param)
        result = requests.post(url=urlstr,params=param)
        print(result.text)

    # 校验
    # print(result.json()['errorCode'],expect)

    if result.status_code == 200 and result.json()['errorCode'] == expect:
        print('请求成功')

    else:
        print('请求失败')
