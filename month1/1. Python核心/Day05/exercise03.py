list1 = []
i = 0
while True:
    num = input("请输入整数：")
    if num == "":
        break
    else:
        list1.append(int(num))
while i < len(list1):
    if list1[i] % 2 == 0:
        i += 1
    else:
        del list1[i]
print(list1)
