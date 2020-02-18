list1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(list1[2][1])

for i in range(len(list1[1]) - 1, -1, -1):
    print(list1[1][i])

for i in list1:
    print(i[2])

for item in list1:
    for i in item:
        print(i, end=" ")
    print()

# for r in range(len(list1)):
#     for c in range(len(list1[r])):
#         print(list1[r][c], end=" ")
#     print()
