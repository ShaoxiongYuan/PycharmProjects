list1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

list2 = []
for c in range(len(list1[0])):
    list3 = []
    for r in range(len(list1)):
        list3.append(list1[r][c])
    list2.append(list3)

print(list2)
