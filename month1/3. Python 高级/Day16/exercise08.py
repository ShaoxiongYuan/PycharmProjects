from common.iterable_tools import IterableHelper


class Wife:
    def __init__(self, name, face_score, money, age):
        self.name = name
        self.face_score = face_score
        self.money = money
        self.age = age


list_wives = [
    Wife("建宁", 86, 999999, 25),
    Wife("双儿", 95, 5000, 23),
    Wife("苏荃", 98, 10000, 30),
    Wife("阿珂", 100, 6000, 23),
    Wife("铁锤", 80, 0, 35),
]

for i in IterableHelper().find_all_no_condition(list_wives, lambda item: item.name):
    print(i)

for i in IterableHelper().find_all_no_condition(list_wives, lambda item: (item.name, item.face_score)):
    print(i)

print(IterableHelper().find_maximum(list_wives, lambda item: item.money))

IterableHelper().sort(list_wives, lambda item: item.face_score)
for item in list_wives:
    print(item.__dict__)
