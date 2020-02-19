start_num = int(input("请输入起始值："))
end_num = int(input("请输入结束值："))

# if start_num < end_num:
#     while start_num < end_num - 1:
#         start_num += 1
#         print(start_num)
#
# elif start_num > end_num:
#     while start_num > end_num + 1:
#         start_num -= 1
#         print(start_num)
# else:
#     print("请输入不一样的值")


# while start_num < end_num - 1:
#     start_num += 1
#     print(start_num)
# while start_num > end_num + 1:
#     start_num -= 1
#     print(start_num)


dir = 1 if start_num < end_num else -1
while start_num != end_num - dir:
    start_num += dir
    print(start_num)
