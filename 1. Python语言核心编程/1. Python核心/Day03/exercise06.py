state = "奇数" if int(input("请输入一个数：")) % 2 else "偶数"
year = int(input("请输入年份："))
code1 = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
print(state)
print(code1)
