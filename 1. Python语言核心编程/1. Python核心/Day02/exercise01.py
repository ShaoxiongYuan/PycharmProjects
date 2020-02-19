def swap(variable01, variable02):
    """

    :param variable01:
    :param variable02:
    :return:
    """
    temp = variable01
    variable01 = variable02
    variable02 = temp
    return variable01, variable02


print(swap("八戒", "沙僧"))
