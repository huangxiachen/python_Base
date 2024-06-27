# 转换成int类型int(x,base)(用于将一个字符串或数字转换为10进制整型。)
#x -- 字符串或数字。base -- 进制数，默认十进制。

#若 x 为纯数字，则不能有 base 参数，否则报错；其作用为对入参 x 取整
# float_var = 3.5678
# print(int(float_var))
# binary_a = int('10001',2)
# print(binary_a)
# six_b = int('0xa',16)
# print(six_b)
# eight_c = int('0123',8)
# print(eight_c)
# error_a = int('0789',8)#报错invalid literal for int() with base 8: '0789'
# print(error_a)

#tuple 函数将可迭代系列（如列表）转换为元组。
#字符串-->元组
str_tuple = tuple('hello')
print(str_tuple)#('h', 'e', 'l', 'l', 'o')
#列表-->元组
list_tuple = tuple([1,2,3,5])
print(list_tuple)
#字典-->元组
dict_tuple = tuple({'a':1,'b':2})
print(dict_tuple)## 将字典转换为元组时，只保留键！
#集合-->元组
set_tuple = tuple({1,2,3,4})
print(set_tuple)

# list() 方法用于将元组或字符串转换为列表
list_str = list('hello')
print(list_str)
list_tuple = list((1,2,3,4))
print(list_tuple)

#set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
#字符串-->集合
set_str = set('hello')
print(set_str)
#字典-->集合
print(set({'a':1,'b':2}))# 将集合转换为集合时，只保留键！
#列表-->集合
print(set([1,2,3,456,57]))
