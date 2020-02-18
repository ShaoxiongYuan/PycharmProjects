length = int(input("请输入斐波那契数列长度："))
list1 = [1, 1]
for _ in range(length - 2):
    list1.append(list1[-2] + list1[-1])
print(list1)
