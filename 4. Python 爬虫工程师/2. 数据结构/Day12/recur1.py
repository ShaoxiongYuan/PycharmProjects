# def f(n):
#     if n == 0:
#         return
#     print(n)
#     f(n - 1)
#
#
# f(3)


# def f(n):
#     if n == 0:
#         return
#     f(n - 1)
#     print(n)
#
#
# f(3)

import sys

sys.setrecursionlimit(100000)


# 打印 1+2+3+...+n 的和
# def sumn(n):
#     if n == 0:
#         return 0
#     return n + sumn(n - 1)
#
#
# print(sumn(1000))

# 使用递归求出 n 的阶乘
def fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)


print(fac(100))
