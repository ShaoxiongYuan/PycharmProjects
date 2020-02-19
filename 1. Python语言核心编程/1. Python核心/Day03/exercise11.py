# import random
#
# num = random.randint(1, 100)
# while True:
#     guess = int(input("请输入："))
#     if guess < num:
#         print("小了")
#     elif guess > num:
#         print("大了")
#     else:
#         print("猜对了")
#         break


"""
最多猜n次
"""
import random

num = random.randint(1, 100)
n = int(input("最多猜几次："))
count = 0
while count < n:
    count += 1
    guess = int(input("请输入："))
    if guess < num:
        print("小了")
    elif guess > num:
        print("大了")
    else:
        print("猜对了")
        break
else:
    print("游戏结束！")
