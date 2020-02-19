def my_zip(iterable1, iterable2, iterable3):
    for i in range(len(iterable1)):
        yield iterable1[i], iterable2[i], iterable3[i]


list1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

for i in zip(*list1):
    print(i)


