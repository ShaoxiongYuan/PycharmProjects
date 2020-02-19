class EmployeeManager:
    def __init__(self):
        self.__list_employees = []

    def add_employees(self, employee):
        self.__list_employees.append(employee)

    def get_total_cost(self):
        total_salary = 0
        for item in self.__list_employees:
            total_salary += item.calculate_salary()
        return total_salary


class Employee:
    def __init__(self, base_salary=0):
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class Coder(Employee):
    def __init__(self, base_salary=0, dividend=0):
        super().__init__(base_salary)
        self.dividend = dividend

    def calculate_salary(self):
        return super().calculate_salary() + self.dividend


class Tester(Employee):
    def __init__(self, base_salary=0, num_of_bugs=0):
        super().__init__(base_salary)
        self.num_of_bugs = num_of_bugs

    def calculate_salary(self):
        return super().calculate_salary() + self.num_of_bugs * 5


c1 = EmployeeManager()
c1.add_employees(Coder(5000, 50))
c1.add_employees(Tester(10000, 5))
print(c1.get_total_cost())
