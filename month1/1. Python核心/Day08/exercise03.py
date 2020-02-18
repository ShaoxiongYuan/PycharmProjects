def del_same_element(list_target):
    """

    :param list_target:
    :return:
    """
    for i in range(len(list_target) - 1, -1, -1):
        for a in range(i):
            if list_target[i] == list_target[a]:
                del list_target[i]
                break


list1 = [34, 8, 56, 9, 8, 9]
del_same_element(list1)
print(list1)
