def is_prime(i):
    """

    :param i:
    :return:
    """
    for a in range(2, i):
        if i % a == 0:
            return False
    return True


def all_prime_number(start, end):
    """

    :param start:
    :param end:
    :return:
    """
    return [item for item in range(start, end + 1) if is_prime(item)]


print(all_prime_number(3, 20))
