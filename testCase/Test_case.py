# coding:utf-8
__author__ = 'lenovo'

# 1.调用readExcel模块，拿到测试数据
# 2.根据接口的请求方式来判断调用xx方法（get请求/post请求） -- 循环
# 3.校验get请求/post请求的数据
# 4.保存执行结果
# 5.写入excel中（writeExcel模块）

# 使用ddt框架实现
import requests,unittest,json
from ddt import ddt,data,unpack
from common.readExcel import readExcel
from common.writeExcel import writeExcel
from common.configHttp import ConfigHttp

# 1--读取excel数据
d = readExcel()  # 实例化
testda = d.assembleData()
# print(testda)
# 实例化，以备调用封装好的requests方法
re = ConfigHttp
# 实例化，以备调用写入excel方法
wr = writeExcel

@ddt
class Mytestcase1(unittest.TestCase):
    @data(*testda)
    @unpack
    def test_nomal(self,id,url,method,param,expect):
        print(id,url,method,param,expect)
        print(type(eval(param)))
        result = re.getRequest(url,method,param)
        # 将response解码成python对象：dict
        real = str(json.loads(result)['errorCode'])
        try:
            status = self.assertEqual(real,expect)
            print('返回结果',status)
            # status = None
        except AssertionError as msg:
            print(msg)
            status = 'Error'
        finally:
            if status == None:
                wr.writeData(id,real,'Success')
            else:
                wr.writeData(id,real,'Fail')

if __name__=='__main__':
    unittest.main


# import requests
# # 1.调用readExcel模块，拿到测试数据
# from common.readExcel import readExcel
# d = readExcel()  # 实例化
# data = d.assembleData()
# # print(data)
#
# # 2.根据接口的请求方式来判断调用xx方法（get请求/post请求）
# for i in data:
#     print(i)
#     print(i[3])
#     method = i[3]
#     urlstr = i[1]
#     param = eval(i[4])
#     expect = int(i[-1])
#     url = i[1]
#
#     if method == 'post':
#         result = requests.post(url=urlstr,data=param)
#         print(result.text)
#     elif method == 'get':
#         result = requests.get(url=urlstr,params=param)
#         print(result.text)
#
#     # 校验
#     # print((result.json()['errorCode']),expect)
#
#     if result.status_code == 200 and result.json()['errorCode'] == expect:
#         print('请求成功')
#     else:
#         print('请求失败')
#
#


