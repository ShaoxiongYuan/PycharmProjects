while True:
    num = input("请输入一个整数：")
    if num == "":
        break
    count = 0
    for item in num:
        count += int(item)
    print(count)
