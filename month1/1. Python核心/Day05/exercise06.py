list1 = []
while True:
    str_input = input("请输入字符串：")
    if str_input == "":
        break
    list1.append(str_input)
print("".join(list1))
