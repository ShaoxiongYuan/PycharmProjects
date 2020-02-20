list1 = [1, 3, 5, 4, 9, 6]
for i in range(len(list1) - 1):
    for a in range(i + 1, len(list1)):
        if list1[i] > list1[a]:
            list1[i], list1[a] = list1[a], list1[i]

print(list1)
