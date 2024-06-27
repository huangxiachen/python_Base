# 输入三个整数x,y,z，请把这三个数由小到大输出。

print('请输入3个数,使用空格隔开:')
numbers = input().split()
for i in range(0,len(numbers)) :
    numbers[i] = int(numbers[i])
# print(sorted(numbers))
print(numbers)
if(int(numbers[0]) > int(numbers[1])) :
#     # temp = numbers[0]
#     # numbers[0] = numbers[1]
#     # numbers[1] = temp
    numbers[0],numbers[1] = numbers[1],numbers[0]
if(int(numbers[0]) > int(numbers[2])) :
#     temp = numbers[0]
#     numbers[0] = numbers[2]
#     numbers[2] = temp
    numbers[0],numbers[2] = numbers[2],numbers[0]
if(int(numbers[1]) > int(numbers[2])) :
#     temp = numbers[1]
#     numbers[1] = numbers[2]
#     numbers[2] = temp
    numbers[1],numbers[2] = numbers[2],numbers[1]
print(numbers)