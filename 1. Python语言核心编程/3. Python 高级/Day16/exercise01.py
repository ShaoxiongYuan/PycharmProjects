def my_enumerate(data):
    index = -1
    for item in data:
        index += 1
        yield index, item


list1 = ["唐僧", "八戒", "悟空"]
for item in my_enumerate(list1):
    print(item)
