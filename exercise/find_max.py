# def find_highest_number(numbers_list):
#     # 此处编写代码
#     k = numbers_list[-1]
#     if len(numbers_list) == 1:
#         return k
#     if k >= numbers_list[-2]:
#         numbers_list.pop(-2)
#         return find_highest_number(numbers_list)
#     else:
#         numbers_list.pop()
#         return find_highest_number(numbers_list)


# # 6 4 9 1 7 12 5
# # 输入数字并转为列表
# numbers_list = list(map(int, input().split()))
# # 调用函数打印结果
# print(find_highest_number(numbers_list))
# print(str(3))

# 错误写法
def get_all_permutations(digits):
    # 在此处编写你的代码
    k = min(digits)
    print(k,end='')
    digits.remove(k)
    if len(digits) == 1:
        return k
    return k+get_all_permutations(digits[1:])


# 获取整数输入并将其转换为列表
digits = list(map(int, input().split()))
# 调用函数
get_all_permutations(digits)