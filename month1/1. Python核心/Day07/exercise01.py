list1 = ["齐天大圣", "八戒", "唐三藏"]

dict1 = {item: len(item) for item in list1}
print(dict1)

list2 = ["张无忌", "赵敏", "周芷若"]
list3 = [101, 102, 103]

dict2 = {list2[i]: list3[i] for i in range(len(list2))}
print(dict2)

dict3 = {v: k for k, v in dict2.items()}
print(dict3)
