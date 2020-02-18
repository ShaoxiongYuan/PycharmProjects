def square_matrix_transpose(num):
    """

    :param num:
    :return:
    """
    list1 = []
    count = 0
    for i in range(num):
        list2 = []
        for a in range(num):
            count += 1
            list2.append(count)
        list1.append(list2)
    for a in range(num - 1):
        for b in range(a + 1, num):
            list1[a][b], list1[b][a] = list1[b][a], list1[a][b]

    return list1


int_input = int(input("请输入方阵长度："))
print(square_matrix_transpose(int_input))
