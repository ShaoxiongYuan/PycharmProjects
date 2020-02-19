year = int(input("请输入年:"))
month = int(input("请输入月："))
day = int(input("请输入日："))

day_2 = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
days = (31, day_2, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


# day_total=0
# for i in range(month-1):
#     day_total+=days[i]

day_total = sum(days[:month - 1:])

print(day_total + day)
