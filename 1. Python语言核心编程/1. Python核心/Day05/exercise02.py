list_name = []
while True:
    name = input("请输入名字：")
    if name == "":
        break
    if name not in list_name:
        list_name.append(name)
    else:
        print("不录入")
for i in range(len(list_name) - 1, -1, -1):
    print(list_name[i])
