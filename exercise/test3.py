# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
import math
for i in range(0,10000) :
    for j in range(10,10000) :
        if j**2 == i + 100 :
            # print(f'j*j={j}*{j}  i={i}')
            for k in range(int(math.sqrt(268)),10000) :
                if k ** 2 == i + 168 + 100 :
                     print(f'k*k={k}*{k}  i={i}')
                     break
            break
print(math.sqrt(256))
print(math.sqrt(324))