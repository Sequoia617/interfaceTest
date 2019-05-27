# coding:utf-8
__author__ = 'lenovo'

# 1.调用readExcel模块，拿到测试数据
# 2.根据接口的请求方式来判断调用xx方法（get请求/post请求） -- 循环
# 3.校验get请求/post请求的数据
# 4.保存执行结果
# 5.写入excel中（writeExcel模块）

import requests

# 1.调用readExcel模块，拿到测试数据
from common.readExcel import readExcel
d = readExcel()  # 实例化
data = d.assembleData()
# print(data)

# 2.根据接口的请求方式来判断调用xx方法（get请求/post请求）
for i in data:
    print(i)
    print(i[3])
    method = i[3]
    urlstr = i[1]
    param = eval(i[4])
    expect = int(i[-1])
    url = i[1]

    if method == 'post':
        result = requests.post(url=urlstr,data=param)
        print(result.text)
    elif method == 'get':
        result = requests.get(url=urlstr,params=param)
        print(result.text)

    # 校验
    # print((result.json()['errorCode']),expect)

    if result.status_code == 200 and result.json()['errorCode'] == expect:
        print('请求成功')
    else:
        print('请求失败')





