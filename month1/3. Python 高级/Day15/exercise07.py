class ShapeManager:
    def __init__(self):
        self.__shape_list = []

    def add_shape(self, shape):
        self.__shape_list.append(shape)

    def __iter__(self):
        for item in self.__shape_list:
            yield item


manager = ShapeManager()
manager.add_shape("圆形")
manager.add_shape("长方形")
manager.add_shape("正方形")

for i in manager:
    print(i)
