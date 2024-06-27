#1.列表推导式
import math


list_infer = [item for item in range(1,6)]
print(list_infer)
list_infer = [item for item in range(1,20) if item % 2 == 0]
print(list_infer)
#2.元组推导式
tuple_infer = tuple((item for item in range(1,6)))
print(tuple_infer)
#3.集合推导式
set_infer = {item for item in {'mike':18,'Mary':20} }
print(set_infer)
#4.字典推导式
ditc_infer = {key:value for key,value in {'mike':18,'Mary':20}.items() if value == 20}
print(ditc_infer)
print(int(math.sqrt(13)))