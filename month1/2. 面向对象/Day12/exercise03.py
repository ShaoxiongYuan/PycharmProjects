class Grenade:
    def explode(self, thing):
        print("手雷爆炸了")
        thing.damage()


class Thing:
    def damage(self):
        pass


class Player(Thing):
    def damage(self):
        print("玩家受到伤害！")


class Enemy(Thing):
    def damage(self):
        print("敌人受到伤害！")


class Duck(Thing):
    def damage(self):
        print("鸭子上天了！")


class House(Thing):
    def damage(self):
        print("房子塌了！")


g1 = Grenade()
p1 = Player()
e1 = Enemy()
d1 = Duck()
h1 = House()
g1.explode(p1)
g1.explode(e1)
g1.explode(d1)
g1.explode(h1)
