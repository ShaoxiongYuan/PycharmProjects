class ShapeIterable:
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        self.__index += 1
        if self.__index > len(self.__data) - 1:
            raise StopIteration()
        return self.__data[self.__index]


class ShapeManager:
    def __init__(self):
        self.__shape_list = []

    def add_shape(self, shape):
        self.__shape_list.append(shape)

    def __iter__(self):
        return ShapeIterable(self.__shape_list)


manager = ShapeManager()
manager.add_shape("圆形")
manager.add_shape("长方形")
manager.add_shape("正方形")


for i in manager:
    print(i)

# iterable1 = manager.__iter__()
# while True:
#     try:
#         item = iterable1.__next__()
#         print(item)
#     except StopIteration:
#         break
