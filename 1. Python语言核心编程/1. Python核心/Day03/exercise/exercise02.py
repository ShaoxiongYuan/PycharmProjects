height = float(input("请输入身高："))
weight = float(input("请输入体重："))
bmi = weight / height ** 2
if 0 < bmi < 18.5:
    print("体重过轻")
elif bmi < 24:
    print("体重正常")
elif bmi < 28:
    print("超重")
elif bmi < 30:
    print("I度肥胖")
elif bmi < 40:
    print("II度肥胖")
else:
    print("III度肥胖")
