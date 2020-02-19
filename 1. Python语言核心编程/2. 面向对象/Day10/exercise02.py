class Wife:
    count = 0

    @classmethod
    def print_count(cls):
        print(f"娶了{cls.count}个老婆")

    def __init__(self, name=""):
        self.name = name
        Wife.count += 1


w1 = Wife("一")
w2 = Wife("二")
Wife.print_count()
