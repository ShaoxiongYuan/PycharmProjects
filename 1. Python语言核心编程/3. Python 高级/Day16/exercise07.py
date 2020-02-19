from common.iterable_tools import IterableHelper


class Wife:
    def __init__(self, name, face_score, money, age):
        self.name = name
        self.face_score = face_score
        self.money = money
        self.age = age


list_wives = [
    Wife("建宁", 86, 999999, 25),
    Wife("双儿", 100, 5000, 23),
    Wife("苏荃", 98, 10000, 30),
    Wife("阿珂", 100, 6000, 23),
    Wife("铁锤", 80, 0, 35),
]

print(IterableHelper.find_single(list_wives, lambda item: item.name == "苏荃"))

print(IterableHelper.find_single(list_wives, lambda item: item.face_score == 100))
