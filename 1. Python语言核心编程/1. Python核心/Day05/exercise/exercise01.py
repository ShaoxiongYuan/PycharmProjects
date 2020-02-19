import random

"""
系统生成随机号码
"""
list0 = []
while len(list0) < 6:
    num1 = random.randint(1, 33)
    if num1 not in list0:
        list0.append(num1)

num2 = random.randint(1, 16)
list0.append(num2)
print(list0)

list1 = []
while len(list1) < 6:
    num3 = int(input(f"请输入第{len(list1) + 1}个蓝色球数："))
    if num3 < 1 or num3 > 33:
        print("超出范围")
    else:
        if num3 not in list1:
            list1.append(num3)
        else:
            print("不能一样")

while True:
    num4 = int(input("请输入红色球数："))
    if num4 < 1 or num4 > 16:
        print("超出范围")
    else:
        list1.append(num4)
        break

i_1 = 0
while i_1 < 6:
    if list1[i_1] in list0[:6:]:
        i_1 += 1
    else:
        print("没有中奖")
        break
else:
    if list1[6] == list0[6]:
        print("中奖了")
    else:
        print("没有中奖")
