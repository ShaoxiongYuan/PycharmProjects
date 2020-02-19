from student_manager_system.bll import StudentManagerController
from student_manager_system.model import StudentModel


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
            self.__modify_students()

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
        self.__manager.remove_students(student_id)

    def __modify_students(self):
        stu = StudentModel()
        stu.id = input("请输入姓名：")
        stu.name = input("请输入姓名：")
        stu.sex = input("请输入性别：")
        stu.age = int(input("请输入年龄："))
        stu.score = int(input("请输入成绩："))
        self.__manager.update_student(stu)