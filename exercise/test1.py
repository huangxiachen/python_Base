# 有四个数字:1、2、3、4,能组成多少个互不相同且无重复数字的三位数？各是多少？
count = 0
for i in range(1,5):
    for j in range(1,5):
        if(j == i):
            continue
        for k in range(1,5):
            if(k == i or k == j):
                continue
            count+=1
            print(f'{i}{j}{k}',end=' ')
print(f'\n{count}')
            

    

    
