class StudentManagerController:
    __init_id = 1000
    """
        核心逻辑(控制)
    """

    @classmethod
    def generate_id(cls, stu):
        stu.id = cls.__init_id
        cls.__init_id += 1

    def __init__(self):
        self.__list_stu = []

    def add_student(self, stu_target):
        StudentManagerController.generate_id(stu_target)
        self.__list_stu.append(stu_target)

    @property
    def list_stu(self):
        return self.__list_stu

    def update_student(self, stu):
        for item in self.list_stu:
            if item.id == stu.id:
                item.name = stu.name
                item.sex = stu.sex
                item.age = stu.age
                item.score = stu.score

    def remove_students(self, id):
        for i in self.__list_stu:
            if i.id == id:
                self.__list_stu.remove(i)
                return True
        return False