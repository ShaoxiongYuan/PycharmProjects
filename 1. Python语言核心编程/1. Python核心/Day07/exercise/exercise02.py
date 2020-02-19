def if_same_element(target_list):
    """
    判断列表中是否有相同元素
    :param target_list: 一个列表
    :return: 是否有相同元素
    """

    # result = False
    for i in range(len(target_list) - 1):
        for a in range(i + 1, len(target_list)):
            if target_list[i] == target_list[a]:
                return True
                # result = True
                # break
        # if result:
        #     break
    return False


list1 = [34, 8, 56, 9, 8, 9]
print(if_same_element(list1))
