list1 = ["唐僧", "猪八戒", "悟空"]

for i, item in enumerate(list1):
    if len(item) > 2:
        list1[i] = ""

print(list1)
