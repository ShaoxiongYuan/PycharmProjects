from common.iterable_tools import IterableHelper


class Wife:
    def __init__(self, name, face_score, money, age):
        self.name = name
        self.face_score = face_score
        self.money = money
        self.age = age


list_wifes = [
    Wife("建宁", 86, 999999, 25),
    Wife("双儿", 95, 5000, 23),
    Wife("苏荃", 98, 10000, 30),
    Wife("阿珂", 100, 6000, 23),
    Wife("铁锤", 80, 0, 35),
]

# def condition1(item):
#     return item.face_score > 90
#
#
# def condition2(item):
#     return item.money < 100000
#
#
# def find(func):
#     for item in list_wifes:
#         if func(item):
#             yield item.__dict__
#
#
# for item in find(condition1):
#     print(item)
#
# for item in find(condition2):
#     print(item)

for i in IterableHelper.find_all(list_wifes, lambda item: item.face_score > 90):
    print(i)

for i in IterableHelper.find_all(list_wifes, lambda item: item.money < 100000):
    print(i)
