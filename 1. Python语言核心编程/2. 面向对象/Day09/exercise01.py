class Dog():
    """
    🐕🐕🐕🐕🐕
    """

    def __init__(self, name, age, color, variety):
        self.name = name
        self.age = age
        self.color = color
        self.variety = variety

    def eat(self):
        print(self.name, "吃鸡腿")

    def sit(self):
        print(self.name, "坐下")


tom = Dog("汤姆", 3, "黄色", "金毛")
jerry = Dog("杰瑞", 5, "黑色", "拉布拉多")
print(tom.name)
print(jerry.variety)
tom.eat()
jerry.sit()
