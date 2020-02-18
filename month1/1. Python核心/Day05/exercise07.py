str_input = input("请输入英文语句：")
list1 = str_input.split(" ")
list2 = list1[::-1]
print(" ".join(list2))
