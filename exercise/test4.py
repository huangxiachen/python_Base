# 输入某年某月某日，判断这一天是这一年的第几天？

# 判断是否是闰年
monthes = (29,31,28,31,30,31,30,31,31,30,31,30,31)
print('请输入年份:')
year = int(input())
print('请输入月份:')
month = int(input())
print('请输入天数:')
day = int(input())
days = day
if(year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)) :
    monthes[2] = 29
for i in range(1,month) :
    days += monthes[i]
print(f'{year}-{month}-{day}是{year}年的第{days}天')

    
