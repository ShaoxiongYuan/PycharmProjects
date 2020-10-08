import turtle
from turtle import Turtle
from random import randint

# 窗口初始化
window = turtle.Screen()  # 返回默认大小(400,300)
window.title("龟兔赛跑")
turtle.bgcolor("forestgreen")
turtle.color("white")
turtle.speed(0)
turtle.penup()
turtle.setpos(-100, 200)
turtle.write("龟兔赛跑", font=("Arial", 30, "bold"))
turtle.penup()

# 设计界面
turtle.setpos(-480, -180)
turtle.color("chocolate")
turtle.begin_fill()
turtle.pendown()
turtle.forward(1000)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(1000)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.end_fill()

# 起点线
turtle.penup()
turtle.setpos(-300, 150)
turtle.color("black")
turtle.begin_fill()
turtle.pendown()
turtle.forward(70)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(70)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.end_fill()

# 终点线
stamp_size = 20
square_size = 15
finish_line = 200

turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size / stamp_size)
turtle.penup()
for i in range(10):
    turtle.setpos(finish_line, (150 - (i * square_size * 2)))
    turtle.stamp()

for j in range(10):
    turtle.setpos(finish_line + square_size, ((150 - square_size) - (j * square_size * 2)))
    turtle.stamp()


def turtle_make(turtle_name, colors, position):
    turtle_name.speed(0)
    turtle_name.color(colors)
    turtle_name.shape("turtle")
    turtle_name.penup()
    turtle_name.goto(position)
    turtle_name.pendown()


# 乌龟初始化
turtle1 = Turtle()
turtle_make(turtle1, "magenta", (-250, 100))
turtle2 = Turtle()
turtle_make(turtle2, "LemonChiffon4", (-250, 50))
turtle3 = Turtle()
turtle_make(turtle3, "RosyBrown2", (-250, 0))
turtle4 = Turtle()
turtle_make(turtle4, "PaleVioletRed1", (-250, -50))

# 兔子  替换图标
turtle.speed(0)
turtle.setpos(-250, -100)
turtle.register_shape("tuzi.gif")
turtle.shape("tuzi.gif")
turtle.penup()
turtle.goto(-250, -100)
turtle.pendown()

# 显示第一名
chengji = Turtle()
chengji.penup()
chengji.color("red")
chengji.setpos(-200, 300)

for i in range(145):
    turtle1.forward(randint(1, 5))
    turtle2.forward(randint(1, 5))
    turtle3.forward(randint(1, 5))
    turtle4.forward(randint(1, 5))
    if randint(1, 5) <= 2:
        turtle.forward(randint(4, 8))
    else:
        pass  # 睡觉
    if turtle1.xcor() >= 205:
        chengji.pendown()
        chengji.write("turtle1获得冠军", font=("Arial", 40, "bold"))
        break
    if turtle2.xcor() >= 205:
        chengji.pendown()
        chengji.write("turtle2获得冠军", font=("Arial", 40, "bold"))
        break
    if turtle3.xcor() >= 205:
        chengji.pendown()
        chengji.write("turtle3获得冠军", font=("Arial", 40, "bold"))
        break
    if turtle4.xcor() >= 205:
        chengji.pendown()
        chengji.write("turtle4获得冠军", font=("Arial", 40, "bold"))
        break
    if turtle.xcor() >= 205:
        chengji.pendown()
        chengji.write("兔子获得冠军", font=("Arial", 40, "bold"))
        break

turtle.done()
