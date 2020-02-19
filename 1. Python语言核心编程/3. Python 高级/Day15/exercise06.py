class MyRangeIterator:
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        self.__index += 1
        if self.__index > self.__data - 1:
            raise StopIteration()
        return self.__index


class MyRange:
    def __init__(self, number):
        self.__number = number

    def __iter__(self):
        return MyRangeIterator(self.__number)


for item in MyRange(999999999999999999999999999):
    print(item)

# manager = MyRange(5).__iter__()
# while True:
#     try:
#         item = manager.__next__()
#         print(item)
#     except StopIteration:
#         break
