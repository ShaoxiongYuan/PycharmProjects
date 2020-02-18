def print_two_dim_list(target_list):
    """
    将二位列表以表格形式打出来
    :param target_list: 一个列表
    """
    for item in target_list:
        for i in item:
            print(i, end="\t")
        print()


list1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print_two_dim_list(list1)
