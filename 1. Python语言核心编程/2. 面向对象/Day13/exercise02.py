class Skill:
    def __init__(self, name="", duration=0, attack=0, consume=0):
        self.name = name
        self.duration = duration
        self.attack = attack
        self.consume = consume

    def __str__(self):
        return "技能名称：%s，时间：%d，攻击力：%d，消耗法力：%d" % (self.name, self.duration, self.attack, self.consume)

    def __repr__(self):
        return 'Skill("%s",%d,%d,%d)' % (self.name, self.duration, self.attack, self.consume)


s1 = Skill("乾坤大挪移", 10, 500, 200)
print(s1)
str_code = s1.__repr__()
s2 = eval(str_code)
s1.name = "九阴白骨爪"
print(s1)
print(s2)
