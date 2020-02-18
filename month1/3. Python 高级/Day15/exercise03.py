tuple1 = ("悟空", "八戒", "唐僧")
dict1 = {"悟空": 101, "八戒": 102, "唐僧": 103}

iterator1 = tuple1.__iter__()
while True:
    try:
        print(iterator1.__next__())
    except StopIteration:
        break

iterator2 = dict1.__iter__()
while True:
    try:
        key = iterator2.__next__()
        print(key, dict1[key])
    except StopIteration:
        break
