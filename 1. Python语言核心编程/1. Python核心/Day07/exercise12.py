def print_range(score):
    """

    :param score:
    :return:
    """
    if 0 <= score < 60:
        return "不及格"
    if score < 70:
        return "及格"
    if score < 90:
        return "良好"
    if score <= 100:
        return "优秀"
    return "不在范围内"


print(print_range(70))
