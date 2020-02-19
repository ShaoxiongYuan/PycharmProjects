year = int(input("年份："))
month = int(input("月份："))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    if month == 2:
        print("29天")
elif month == 2:
    print("28天")
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("31天")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30天")
else:
    print("月份错误")
