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

d = readExcel()  # 实例化
testda = d.assembleData()
print(testda)
re = ConfigHttp
wr = writeExcel

@ddt
class Mytestcase1(unittest.TestCase):
    @data(*testda)
    @unpack
    def test_nomal(self,id,url,method,param,expect):
        print(id,url,method,param,expect)
        print(type(eval(param)))
        result = re.getRequest(url,method,param)
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


