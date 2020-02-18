month = int(input("请输入月份："))
if 1 <= month <= 3:
    print("春天")
elif 4 <= month <= 6:
    print("夏天")
elif 7 <= month <= 9:
    print("秋天")
elif 10 <= month <= 12:
    print("冬天")
else:
    print("错误")
