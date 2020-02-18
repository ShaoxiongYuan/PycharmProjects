def print_rectangle(side_len, char):
    """
    打印矩形
    :param char: 打印的形状
    :param side_len: 矩形边长（int)
    :return:
    """
    print(char * side_len)
    for i in range(side_len - 2):
        print(char + " " * (side_len - 2) + char)
    print(char * side_len)


print_rectangle(5, "*")
print_rectangle(7, "#")
