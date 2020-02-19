str_input = input("请输入一个字符串：")

# list1 = []
# for i in str_input:
#     if i not in list1:
#         list1.append(i)
#
# for i in list1:
#     count = 0
#     for item in str_input:
#         if item == i:
#             count += 1
#     print(f"{i}出现了{count}次。")

dict1={}
for item in str_input:
    if item in dict1:
        dict1[item]+=1
    else:
        dict1[item]=1
for k,v in dict1.items():
    print(f"{k}出现了{v}次。")