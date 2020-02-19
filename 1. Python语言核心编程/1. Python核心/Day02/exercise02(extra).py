def change(price, amount, paid):
    """

    :param price:
    :param amount:
    :param paid:
    :return:
    """
    return_money = float(paid) - float(amount) * float(price)
    return "应找回" + str(return_money) + "元。"


print(change(9, 7, 100))
