def is_leap_year(y):
    """

    :param y:
    :return:
    """
    return y % 4 == 0 and y % 100 != 0 or y % 400 == 0


def day_number(y, m):
    """

    :param y:
    :param m:
    :return:
    """
    if m == 2:
        return 29 if is_leap_year(y) else 28
    if m in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if m in (4, 6, 9, 11):
        return 30
    return -1


year = int(input("年份："))
month = int(input("月份："))
print(day_number(year, month))
