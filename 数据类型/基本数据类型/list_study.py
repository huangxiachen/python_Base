# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]
 
# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
print(takeSecond(random))
# 指定第二个元素排序
random.sort(key=takeSecond)
 
# 输出类别
print ('排序列表：', random)
print(random.pop(2))