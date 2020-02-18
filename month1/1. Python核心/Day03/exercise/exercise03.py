while True:
    age = input("请输入年龄：")
    if age == "":
        break
    elif not age.isdigit():
        print("错误！")
    else:
        age = int(age)
        if 0 <= age <= 1:
            print("婴儿")
        elif 2 <= age <= 13:
            print("儿童")
        elif 14 <= age <= 20:
            print("青少年")
        elif 21 <= age <= 65:
            print("成年人")
        elif age >= 66:
            print("老年人")
