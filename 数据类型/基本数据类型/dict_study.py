#遍历字典
dict_var = {'name':'Mike','age':18,'gender':'girl'}
# 1.通过字典的键遍历字典
for key in dict_var.keys() :
    print('{}:{}'.format(key,dict_var[key]))
print('------------------------------------')
#2.通过键值对来遍历字典
for key,value in dict_var.items() :
    print('{}:{}'.format(key,value))

#深入理解dict的拷贝方式
dict1 =  {'user':'runoob','num':[1,2,3]}
 
dict2 = dict1          # 浅拷贝: 引用对象
dict3 = dict1.copy()   # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，子对象是引用
 
# 修改 data 数据
dict1['num'].remove(1)
dict1['user']='root'

# 输出结果
print(dict1)
print(dict2)
print(dict3)

print('------------------------------------')

# 修改键
update_newkey = {'new_num':[1,2,3]}
dict1.update(update_newkey)
print(dict1)

print('------------------------------------')

# 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
seq = ['color1','color2','color3']

create_dict = dict.fromkeys(seq,)
print(create_dict)

print('------------------------------------')

# 返回指定键的值，如果键不在字典中返回默认值，如果不指定默认值，则返回 None。
dict_var = {'people1':'Mike','people2':'Mary','people3':'KangKang'}
print(dict_var.get('Honey','不存在'))

# 删除
# 删除字典 key（键）所对应的值，返回被删除的值。
print(dict_var.pop('people1'))
# 返回并删除字典中的最后一对键和值。
print(dict_var.popitem())