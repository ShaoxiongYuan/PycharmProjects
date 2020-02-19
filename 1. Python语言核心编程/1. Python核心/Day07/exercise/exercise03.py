list1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]


def element_in_list(target_list, num):
    """
    查找是否有这个数字
    :param target_list: 一个列表
    :param num: 需要查找的数字，int类型
    :return: 是否有这个数
    """

    for i in target_list:
        if num in i:
            return True
    return False


print(element_in_list(list1, 67))
