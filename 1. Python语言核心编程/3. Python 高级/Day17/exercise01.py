class Skill:
    def __init__(self, name="", duration=0, atk=0, cost_sp=0):
        self.name = name
        self.duration = duration
        self.atk = atk
        self.cost_sp = cost_sp


list_skills = [
    Skill("乾坤大挪移", 50, 200, 500),
    Skill("降龙十八掌", 60, 300, 800),
    Skill("金钟罩", 60, 0, 200),
    Skill("猴子偷桃", 50, 150, 0),
]

for item in map(lambda item: (item.name, item.atk, item.cost_sp), list_skills):
    print(item)

for item in filter(lambda item: item.atk > 200, list_skills):
    print(item.__dict__)

for item in map(lambda skill: skill.name, filter(lambda item: item.duration <= 50, list_skills)):
    print(item)

list1 = [(1, 1), (2,), (3, 3, 3), (4, 4)]
for item in min(list1, key=lambda item: len(item)):
    print(item)

for item in sorted(list_skills, key=lambda item: item.cost_sp, reverse=True):
    print(item.__dict__)
