from turtle import *
import random


def drawTree(length):
    if length > 1:
        if 14 < length < 30:  # 缩小一下树干
            pensize(4)
        elif 5 < length < 15:  # 长度这个范围内那么就是绿叶
            color('#04B486')  #
            pensize(3)
        elif 1 < length < 5:  # 红花
            color('#FE2E9A')
            pensize(2)
        else:
            color('#5E5E5E')  # 其他范围就是正常的树干
            pensize(5)
        # 随机角度与长度
        randangle = 2 * random.random()
        randlen = 2 * random.random()

        # 每次使用函数先绘制线段，再调整角度，这里是向右的角度转动
        fd(length)
        right(20 * randangle)
        drawTree(length - 10 * randlen)

        # 这里是向左的角度转动
        left(40 * randangle)
        drawTree(length - 10 * randlen)

        right(20 * randangle)

        up()
        backward(length)
        down()


def fallingFlowers(m):
    x, y = -1000, -750
    for i in range(30):
        up()
        goto(x, y)
        x += 100
        down()
        yval = 50
        for i in range(m):
            a = 100 * random.random()
            b = 2 * random.random()
            print(a)
            if a > 59:
                color('#FE2E9A')
            else:
                color('#04B486')
            circle(5)
            up()
            goto(x, y + (yval * b))
            fd(a)
            yval += 50
            down()


setworldcoordinates(-1000, -750, 1000, 750)
tracer(200, 1)

fallingFlowers(10)  # 绘制落叶
bgcolor("#F5F6CE")
color('#5E5E5E')
pensize(5)

up()
goto(0, -700)  # 跳到绘制起始点
down()

left(80)
fd(140)
drawTree(120)

input()
