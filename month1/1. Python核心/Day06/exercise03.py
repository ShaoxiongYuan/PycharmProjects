dict1 = {}
while True:
    name = input("请输入学生姓名：")
    if name == "":
        break
    age = input("请输入学生年龄：")
    sex = input("请输入学生性别：")
    score = input("请输入学生成绩：")
    dict1[name] = [age, sex, score]

for k, v in dict1.items():
    print(f"{k}的年龄是{v[0]}，性别是{v[1]}，成绩是{v[2]}。")
if "唐僧" in dict1:
    print(dict1["唐僧"][2])
