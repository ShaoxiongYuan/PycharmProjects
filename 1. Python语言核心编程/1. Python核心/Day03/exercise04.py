score = int(input("请输入成绩："))
if 0 <= score < 60:
    print("不及格")
elif score < 70:
    print("及格")
elif score < 90:
    print("良好")
elif score <= 100:
    print("优秀")
else:
    print("不在范围内")

