"""
    学生信息管理系统
"""


class StudentModel:
    """
        学生模型
    """
    count = 1

    def __init__(self, name="", age=0, sex="", score=0):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = score
        self.id = StudentModel.count
        StudentModel.count += 1

    def print_self(self):
        print(self.name, self.age, self.sex, self.score, self.id)


class StudentManagerView:
    """
        界面视图(逻辑)
    """

    def __init__(self):
        self.__manager = StudentManagerController()

    def __display_menu(self):
        print("1)添加学生信息")
        print("2)显示学生信息")
        print("3)删除学生信息")
        print("4)修改学生信息")

    def __select_menu(self):
        item = input("请输入选项：")
        if item == "1":
            self.__input_students()
        elif item == "2":
            self.__output_students()
        elif item == "3":
            self.__delete_students()
        elif item == "4":
            self.__update_students()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_students(self):
        name = input("请输入姓名：")
        sex = input("请输入性别：")
        age = int(input("请输入年龄："))
        score = int(input("请输入成绩："))
        stu = StudentModel(name, age, sex, score)
        self.__manager.add_student(stu)

    def __output_students(self):
        for i in self.__manager.list_stu:
            i.print_self()

    def __delete_students(self):
        student_id = int(input("需要删除的学生ID："))
        self.__manager.delete_students(student_id)

    def __update_students(self):
        while True:
            self.__output_students()
            id = int(input("需要修改的学生ID，按5退出"))
            if id == 5:
                break
            else:
                self.__manager.change_student(id)


class StudentManagerController:
    """
        核心逻辑(控制)
    """

    def __init__(self):
        self.__list_stu = []

    def add_student(self, stu_target):
        self.__list_stu.append(stu_target)

    @property
    def list_stu(self):
        return self.__list_stu

    def delete_students(self, id):
        for i in self.__list_stu:
            if i.id == id:
                self.__list_stu.remove(i)

    def change_student(self, id):
        for i in self.__list_stu:
            if i.id == id:
                i.print_self()
                change = int(input("修改姓名按1，修改性别按2，修改年龄按3，修改成绩按4"))
                if change == 1:
                    name = input("输入新姓名：")
                    i.name = name
                elif change == 2:
                    sex = input("输入新年龄：")
                    i.sex = sex
                elif change == 3:
                    age = input("请输入新年龄：")
                    i.age = age
                elif change == 4:
                    score = input("请输入新成绩：")
                    i.score = score


view = StudentManagerView()
view.main()
