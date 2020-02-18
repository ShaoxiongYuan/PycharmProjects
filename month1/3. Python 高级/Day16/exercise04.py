list1 = [10, "悟空", 80, 33, 20, "八戒", 25]

for item in (item for item in list1 if type(item) == str):
    print(item)

for item in (item for item in list1 if type(item) == int and item % 2 == 0):
    print(item)
