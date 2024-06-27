'''
int、(long)、float、bool、complex(复数)
'''
import math

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
# Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， 
# True==1、False==0 会返回 True，但可以通过 is 来判断类型。
print(True+1)
# 使用complex(a,b)创建复数，实部 a 和虚部 b 都是浮点型。
complex_var = complex(2,3.3)#(2+3.3j)
print(complex_var+3)

# 保留n位小数的方法
# 1.使用格式化字符串： 使用%.nf格式化字符串，其中n表示要保留的小数位数。
float_var1 = 2.3383
formatted_var1 = '%.2f'%float_var1#保留两位小数(四舍五入)
print(f'使用"%.nf格式化字符串":{formatted_var1}')
#2.使用format()函数： 使用format()函数同样可以实现四舍五入并保留指定小数位数。
formatted_var1 = format(float_var1,'.2f')
print(f'使用format()函数:{formatted_var1}')
#3.使用 Python 中的 f-string 来保留小数点后的固定位
print(f'f-string 来保留小数:{float_var1:.2f}')
#4.使用round()函数： round()函数可以精确地进行四舍五入，但无法保证相同的小数位数。
print(f'使用round()函数:{round(float_var1,2)}')

#ceil()向上取整(向更大的数取整)
#floor()向下取整(向更小的数取整)
#round()四舍五入(会出现不精确的情况)
print(f'ceil()向上取整:{math.ceil(float_var1)}')
print(f'floor()向下取整:{math.floor(float_var1)}')