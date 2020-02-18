str1 = " 校 训：自 强不息,厚 德载 物 "
# count = 0
# for i in str1:
#     if i == " ":
#         count += 1
# print(count)

"""
计算空格
"""
print(str1.count(" "))

"""
删除前后空格
"""
str2 = str1.strip()
print(str2)

"""
删除所有空格
"""
str3 = str2.replace(" ", "")
print(str3)

"""
查找"不息"的位置
"""
print(str3.find("不息"))
