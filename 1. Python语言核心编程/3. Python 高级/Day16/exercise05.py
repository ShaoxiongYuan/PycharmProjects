class Skill:
    def __init__(self, name="", duration=0, atk=0, cost_sp=0):
        self.name = name
        self.duration = duration
        self.atk = atk
        self.cost_sp = cost_sp

    def __str__(self):
        return "技能名称：%s，时间：%d，攻击力：%d，消耗法力：%d" % (self.name, self.duration, self.atk, self.cost_sp)


list_skills = [
    Skill("乾坤大挪移", 50, 200, 500),
    Skill("降龙十八掌", 60, 300, 800),
    Skill("金钟罩", 60, 0, 200),
    Skill("猴子偷桃", 50, 150, 0),
]


def find1():
    for item in list_skills:
        if item.cost_sp > 300:
            yield item


def find2():
    for item in list_skills:
        if item.duration == 50:
            yield item.name, item.duration


def find3():
    for item in list_skills:
        if item.name == "猴子偷桃":
            return item


for item in find1():
    print(item)
for item in find2():
    print(item)
print(find3())
