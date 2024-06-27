#字符串不可以改变原有字符串中的字符,只能重新赋值
str = 'hello'
# str[1] = 'a'#报错'str' object does not support item assignment
# print(str)
str = 'hello word'
print(str)
#获取字符串长度
print(f'字符串长度为:{len(str)}')
# 遍历字符串
#1.for循环遍历
for c in str :
    print(c,end=' ')
print('\n')

#2.通过访问下标遍历(索引值以 0 为开始值，-1 为从末尾的开始位置。)
for index in range(0,len(str)) :
    print(str[index],end=' ')
print('\n')

for index in range(-len(str),0) :
     print(str[index],end=' ')
print('\n')

#Python 访问子字符串，可以使用方括号 [] 来截取字符串
print(str[:])
print(str[0:])
print(str[:len(str)])
print(str[0:3])
print(str[3:9])
print(type(b'adfsf'))
# import time

# for i in range(101):
#     print("\r{}%".format(i),end=' ')
#     time.sleep(0.05)