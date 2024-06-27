#在字符串中使用变量
#为 f 字符串,f 是 format（设置格式）的简写,因为 Python 通过把花括号内的变量替换为其值来设置字符串的格式
#使用 f 字符串可以完成很多任务,如利用与变量关联的信息来创建完整的消息
first_name = 'Chen'
second_name = 'XiaoHong'
full_name = f'{first_name} {second_name}'
print("完整姓名为: "+full_name)
print(f"Hello,{full_name}")