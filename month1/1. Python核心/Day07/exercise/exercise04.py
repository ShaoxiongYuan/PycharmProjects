list1 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

for a in range(len(list1) - 1):
    for b in range(a + 1, len(list1)):
        list1[a][b], list1[b][a] = list1[b][a], list1[a][b]

print(list1)

"""
分析
"""
# list1[0][1]  list1[1][0]
# list1[0][2]  list1[2][0]
# list1[0][3]  list1[3][0]


# list1[1][2]  list1[2][1]
# list1[1][3]  list1[3][1]

# list1[2][3]  list1[3][2]
