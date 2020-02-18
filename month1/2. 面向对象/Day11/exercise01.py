class Person:
    def __init__(self, money):
        self.money = money


class Bank:
    def __init__(self, money):
        self.money = money

    def withdraw(self, person, value):
        self.money -= value
        person.money += value


xm = Person(0)
zsyh = Bank(100000)
zsyh.withdraw(xm, 5000)
print(xm.money)
print(zsyh.money)
