class Skill:
    def __init__(self, name, time, attack, consume):
        self.name = name
        self.time = time
        self.attack = attack
        self.consume = consume

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        if 1 <= value <= 60:
            self.__time = value
        else:
            raise Exception

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, value):
        if 0 <= value <= 500:
            self.__attack = value
        else:
            raise Exception

    @property
    def consume(self):
        return self.__consume

    @consume.setter
    def consume(self, value):
        if 0 <= value <= 1000:
            self.__consume = value
        else:
            raise Exception

    def print_self(self):
        print(self.name, self.time, self.attack, self.__consume)


skill_list = [
    Skill("降龙十八掌", 20, 550, 200),
    Skill("凌波微步", 20, 300, 250),
    Skill("如来神掌", 55, 50, 30)
]


# 在技能列表中查找攻击力大于100的所有技能名称,攻击力与消耗的法力
def find_attack():
    list_result = []
    for item in skill_list:
        if item.attack > 100:
            list_result.append((item.name, item.attack, item.consume))
    return list_result


# print(find_attack())


# 在技能列表中查找消耗法力最大的技能对象
def find_max_consume():
    max = skill_list[0]
    for i in range(1, len(skill_list)):
        if skill_list[i].consume > max.consume:
            max = skill_list[i]
    return max


# result = find_max_consume()
# result.print_self()


# 在技能列表中删除持续时间大于50的技能对象
def delete_skill():
    count = 0
    for item in range(len(skill_list) - 1, -1, -1):
        if skill_list[item].time > 50:
            del skill_list[item]
            count += 1
    return count


# print(delete_skill())


# 根据消耗的法力对技能列表进行升序排列
def arrange_order():
    for i in range(len(skill_list) - 1):
        for a in range(i + 1, len(skill_list)):
            if skill_list[i].consume > skill_list[a].consume:
                skill_list[i], skill_list[a] = skill_list[a], skill_list[i]


# arrange_order()
# for i in skill_list:
#     i.print_self()


# 将技能列表中攻击力小于100的技能消耗法力设置为0
def set_attack_zero():
    for i in skill_list:
        if i.attack < 100:
            i.consume = 0
    return skill_list


# for i in set_attack_zero():
#     i.print_self()


# 删除技能列表中持续时间相同的技能(只保留一个)
def del_same_element():
    for i in range(len(skill_list) - 1, -1, -1):
        for a in range(i):
            if skill_list[i].time == skill_list[a].time:
                del skill_list[i]
                break

# del_same_element()
# for i in skill_list:
#     i.print_self()
