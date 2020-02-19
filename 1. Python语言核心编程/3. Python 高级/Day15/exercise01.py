def get_score():
    while True:
        try:
            num = int(input("请输入成绩："))
            return num
        except ValueError:
            print("只能输入整数")


print(get_score())
