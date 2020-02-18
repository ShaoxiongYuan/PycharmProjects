class Enemy:
    def __init__(self, name, blood, defense, attack):
        self.name = name
        self.blood = blood
        self.defense = defense
        self.attack = attack

    def injure(self):
        self.blood -= 100

    def print_self(self):
        # print(self.__dict__)
        print(self.name, self.blood, self.defense, self.attack)


list_enemy = [
    Enemy("金", 10, 50, 70),
    Enemy("银", 100, 100, 150),
    Enemy("铜", 150, 30, 10)
]


# list_enemy[1].injure()
# list1 = [i.print_self() for i in list_enemy if i.blood != 0]
# list2 = [{i.name: i.attack} for i in list_enemy if i.attack > 50]
# print(list1)
# print(list2)

def find_min_defense():
    min = list_enemy[0]
    for i in range(1, len(list_enemy)):
        if list_enemy[i].defense < min.defense:
            min.defense = list_enemy[i].defense
    return min


# result = find_min_defense()
# result.print_self()


def delete_enemy():
    count = 0
    for item in range(len(list_enemy) - 1, -1, -1):
        if list_enemy[item].blood > 50:
            del list_enemy[item]
            count += 1
    return count


# print(delete_enemy())


def arrange_order():
    for i in range(len(list_enemy) - 1):
        for a in range(i + 1, len(list_enemy)):
            if list_enemy[i].attack < list_enemy[a].attack:
                list_enemy[i], list_enemy[a] = list_enemy[a], list_enemy[i]

# arrange_order()
# for i in list_enemy:
#     i.print_self()
