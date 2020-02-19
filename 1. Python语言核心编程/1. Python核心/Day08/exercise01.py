def matrix_turn(list_target):
    """

    :param list_target:
    :return:
    """
    list2 = []
    for c in range(len(list_target[0])):
        list3 = []
        for r in range(len(list_target)):
            list3.append(list_target[r][c])
        list2.append(list3)

    return list2


list1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(matrix_turn(list1))
