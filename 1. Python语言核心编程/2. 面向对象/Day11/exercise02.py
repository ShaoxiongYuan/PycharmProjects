class Player:
    def __init__(self, attack):
        self.attack = attack

    def attack_enemy(self, enemy):
        enemy.damage(self.attack)


class Enemy:
    def __init__(self, blood):
        self.blood = blood

    def damage(self, value):
        self.blood -= value
        if self.blood <= 0:
            self.__death()

    def __death(self):
        print("播放死亡动画")


p1 = Player(90)
e1 = Enemy(100)
p1.attack_enemy(e1)
