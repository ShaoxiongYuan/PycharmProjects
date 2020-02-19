def sum_digit(num):
    """

    :param num:
    :return:
    """
    count = 0
    for item in str(num):
        count += int(item)
    return count


print(sum_digit(1234))
