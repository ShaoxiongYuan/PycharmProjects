def arrange_order(list_target):
    """

    :param list_target:
    :return:
    """
    for i in range(len(list_target) - 1):
        for a in range(i + 1, len(list_target)):
            if list_target[i] > list_target[a]:
                list_target[i], list_target[a] = list_target[a], list_target[i]


list1 = [4, 54, 5, 6, 7, 8, 3]
arrange_order(list1)
print(list1)
