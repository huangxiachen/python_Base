'''
集合(set)是一个无序的不重复元素序列。
集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。
可以使用大括号 { } 创建集合，元素之间用逗号 , 分隔， 或者也可以使用 set() 函数创建集合。
'''
# 直接使用大括号创建集合
set_var1 = {'value1','value2','value3'}
# 使用 set() 函数从列表创建集合
set_var2 = set([1,2,3,4])
# 创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
set_none = set()
print(set_var1)
print(set_var2)
print(set_none)
print('---------------------------------------')

#  # 下面展示两个集合间的运算.
a = set('abracadabra')
b = set('alacazam')
# 差集(集合a中包含而集合b中不包含的元素)
print(a-b)
# 并集:集合a或b中包含的所有元素
print(a|b)
# 交集:集合a和b中都包含了的元素
print(a&b)
# 不同时包含于a和b的元素
print(a^b)
print('---------------------------------------')

# copy() 方法用于拷贝一个集合。
c = a.copy()
print(c)

# set只能存储不可变类型：tuple,str
set_var = {'Mike',['swimming','running','pinpong']}
for item in set_var :
    print(item)
