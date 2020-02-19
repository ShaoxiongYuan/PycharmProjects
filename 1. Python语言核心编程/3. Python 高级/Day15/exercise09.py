list1 = [23, 432, 3, 424, 24, 2]


def find_less_than_10(list_target):
    list2 = []
    for item in list_target:
        if item < 10:
            list2.append(i)
    return list2


print(find_less_than_10(list1))


def find_greater_than_10(list_target):
    for item in list_target:
        if item > 10:
            yield item


for i in find_greater_than_10(list1):
    print(i)
