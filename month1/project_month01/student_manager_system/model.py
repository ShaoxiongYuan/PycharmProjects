class StudentModel:
    """
        学生模型
    """

    def __init__(self, name="", age=0, sex="", score=0, id=0):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = score
        self.id = id

    def print_self(self):
        print(self.name, self.age, self.sex, self.score, self.id)