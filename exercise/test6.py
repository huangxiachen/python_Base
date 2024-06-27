# 斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

# count = int (input('输入:'))
# def fib(count) :  
#     if count == 1 :
#         return 0
#     if count == 2 :
#         return 1
#     return fib(count - 1) + fib(count - 2)  
# print(fib(count))

# count = int (input('输入:'))
# def fib(n):
#     if n == 1:
#         return [1]
#     if n == 2:
#         return [1, 1]
#     fibs = [1, 1]
#     for i in range(2, n):
#         fibs.append(fibs[-1] + fibs[-2])
#     return fibs
# print(fib(count))


# number = int (input('输入:'))

# def mutiple(number) :
#     if number == 1 :
#         print (f'{number} = ',end=' ')
#         return 1
#     elif number <= 0 : 
#         return '没有阶层'
#     else :
       
#         print (f'{number} *',end=' ')
#         return number * mutiple(number - 1)
# print(mutiple(number))
# list = [8,2,3,4]
# list.pop()
# print(sorted(list))
# print(list)
# list.sort()
# print(list)
str1 = 'abcd'
str2 = 'hjig'
print(str2<str1)
