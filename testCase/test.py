# coding:utf-8
__author__ = 'lenovo'

# 将三个列表中的元素一一对应整合成一个列表
a= [1,2,3]
b = ['a','b','c']
c = ['4','5','6']
d = list(zip(a,b,c))
print(d)
# print(list(zip(a,b,c)))
#
# lists = map(list,zip(a,c))
# for i in lists:
#     print(i)

# 方法一：
n = []
for a,b,c in d:
    print(a,c)
    n.append((a,c))
print(n)

# 方法二
a = []
for i in d:
    print('---i',i)
    a.append((i[0],i[-1]))
    # a.append(i[1])
    print('---a',a)
