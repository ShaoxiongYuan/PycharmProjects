# 方法一
list1 = [2, 2, 3, 3, 77, 10, 11, 11, 5]
for i in range(len(list1) - 1, -1, -1):
    for a in range(i):
        if list1[i] == list1[a]:
            del list1[i]
            break

print(list1)

# 方法二
list1 = [2, 2, 3, 3, 77, 10, 11, 11, 5]
list2 = []

for i in list1:
    if i not in list2:
        list2.append(i)

print(list2)
