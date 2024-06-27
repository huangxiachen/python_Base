'''
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，
然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
'''
a = [1,2,3]
b = [4,5,56]
zipped = zip(a,b)#接受多个可迭代的对象
print(zipped)#<zip object at 0x0000024D2EF67DC0>输出迭代器对象的存储位置
# 转换
print(list(zipped))
for i,j in zip(a,b):
    print(i,j)
print(range(23))