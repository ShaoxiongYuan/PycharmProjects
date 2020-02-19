text = input("请输入一段文字：")
# list1 = list(text)
# list2 = []
# for i in range(len(list1) - 1, -1, -1):
#     list2.append(list1[i])
#
# if list1 == list2:
#     print("True")
# else:
#     print("False")

result = text == text[::-1]
print(result)
