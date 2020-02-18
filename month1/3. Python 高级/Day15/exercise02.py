class Skill:
    def __init__(self, name="", duration=0):
        self.name = name
        self.duration = duration

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        if 0 <= value <= 60:
            self.__duration = value
        else:
            raise DurationError("时间超出范围", 1000, "if 0 <= value <= 60")


class DurationError(Exception):
    def __init__(self, message="", id=0, code=""):
        self.message = message
        self.id = id
        self.code = code


try:
    s1 = Skill("九阴白骨爪", 90)
except DurationError as d:
    print(d.message)
    print(d.id)
    print(d.code)
