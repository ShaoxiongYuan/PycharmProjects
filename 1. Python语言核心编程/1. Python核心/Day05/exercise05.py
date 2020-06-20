# 方法一
length = int(input("请输入斐波那契数列长度："))
list1 = [1, 1]
for _ in range(length - 2):
    list1.append(list1[-2] + list1[-1])
print(list1)


# 方法二
def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(list(fibonacci(5)))
