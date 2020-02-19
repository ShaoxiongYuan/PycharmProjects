list1 = [4, 54, 5, 6, 7, 8, 3]
for i in range(len(list1) - 1):
    for a in range(i + 1, len(list1)):
        if list1[i] > list1[a]:
            list1[i], list1[a] = list1[a], list1[i]

print(list1)
