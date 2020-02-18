class EmployeeIterable:
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        self.__index += 1
        if self.__index > len(self.__data) - 1:
            raise StopIteration()
        return self.__data[self.__index]


class EmployeeManager:
    def __init__(self):
        self.__employee_list = []

    def add_employee(self, employee):
        self.__employee_list.append(employee)

    def __iter__(self):
        return EmployeeIterable(self.__employee_list)


manager = EmployeeManager()
manager.add_employee("张三")
manager.add_employee("李四")
manager.add_employee("王五")

for item in manager:
    print(item)
