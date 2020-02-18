class Enemy:
    def __init__(self, name="", blood=0, attack=0):
        self.name = name
        self.blood = blood
        self.attack = attack

    def set_blood(self, value):
        if 0 <= value <= 500:
            self.__blood = value
        else:
            raise Exception("血量超出范围")

    def get_blood(self):
        return self.__blood

    def set_attack(self, value):
        if 10 <= value <= 100:
            self.__attack = value
        else:
            raise Exception("攻击力超过范围")

    def get_attack(self):
        return self.__attack

    blood = property(get_blood, set_blood)
    attack = property(get_attack, set_attack)


e1 = Enemy("一", 501, 15)
print(e1.blood)
e2 = Enemy("二", 23, 101)
print(e2.attack)
