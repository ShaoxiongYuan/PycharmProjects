weight1 = float(input("请输入体重："))
weight2 = float(input("请输入体重："))
weight3 = float(input("请输入体重："))
weight4 = float(input("请输入体重："))
max_w = weight1
if max_w < weight2:
    max_w = weight2
if max_w < weight3:
    max_w = weight3
if max_w < weight4:
    max_w = weight4
print(max_w)
