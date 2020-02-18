class MyRange:
    def __init__(self, number):
        self.__number = number

    def __iter__(self):
        for i in range(self.__number):
            yield i


for item in MyRange(5):
    print(item)
