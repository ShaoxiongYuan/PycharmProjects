def func01(*args, **kwargs):
    print(args)
    print(kwargs)


func01(1, 2, 3, a=1, b=2, c=3)
func01()


def func02(a, b=0, *args, c=0, d=0, **kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kwargs)


func02(1, 1, 1, 2, 3, c=1, d=1, e=1, f=2, g=3)
func02(1, 1, 1, 2, 3, c=1, f=2, g=3)
