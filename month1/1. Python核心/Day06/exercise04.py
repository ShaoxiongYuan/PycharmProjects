list1 = []
while True:
    name = input("请输入学生姓名：")
    if name == "":
        break
    age = input("请输入学生年龄：")
    sex = input("请输入学生性别：")
    score = input("请输入学生成绩：")
    dict1 = {"name": name, "age": age, "sex": sex, "score": score}
    list1.append(dict1)

for item in list1:
    print("%s的年龄是%s,性别是%s,分数是%s" % (item["name"], item["age"], item["sex"], item["score"]))
