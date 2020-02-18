list1 = [23, 646, 4, 8, 7, 2, 31, 2, 99999999999999999]
max_value = list1[0]
for i in list1:
    if max_value < i:
        max_value = i
print(max_value)
