class Person:
    def __init__(self, name=""):
        self.name = name

    def teach_skill(self, person, skill):
        print(self.name, "教", person.name, skill)

    def work(self, salary):
        print(self.name, "挣了", salary, "元")


zwj = Person("张无忌")
zm = Person("赵敏")
zwj.teach_skill(zm, "九阳神功")
zm.teach_skill(zwj, "化妆")
zwj.work(8000)
zm.work(10000)
