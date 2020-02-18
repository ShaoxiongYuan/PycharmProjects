"""
形式参数
"""


# 1.位置形参：必选
def func01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


# 2.默认形参：可选
def func02(p1=True, p2="", p3=0):
    print(p1)
    print(p2)
    print(p3)


func02()
func02(False, "a", 10)
func02(p2="A")
func02(False, p3="C")


# 3.星号元组形参：合（位置）
# 以args命名
def func03(*p1):
    print(p1)


func03()
func03(1, 2, 3, 4, 5)
# func03(a=1, b=2)

list1 = [1, 2, 3]
func03(*list1)


# 4.命名关键字形参：必须使用关键字实参
# ✳后面的形参是关键字形参
def func04(*args, p1, p2):
    print(args)
    print(p1)
    print(p2)


func04(1, p1=2, p2=3)
print("悟空", 25, 100, sep="-", end=" ")


def func05(p1, *, p2):
    print(p1)
    print(p2)


func05(1, p2=2)
func05(p1=1, p2=2)


# 5.双星号字典形参：合（关键字实参）
# 以kwargs命名
def func06(**kwargs):
    print(kwargs)


func06(a=1, b=2, c=3)
func06()
