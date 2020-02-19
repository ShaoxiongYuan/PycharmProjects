from math import sqrt


class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "x分量是%d，y分量是%d" % (self.x, self.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other.x, self.y * other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __imul__(self, other):
        self.x *= other.x
        self.y *= other.y
        return self

    def __lt__(self, other):
        return sqrt(self.x ** 2 + self.y ** 2) < sqrt(other.x ** 2 + other.y ** 2)


list_vectors = [
    Vector2(200, 700),
    Vector2(400, 300),
    Vector2(100, 900),
    Vector2(300, 140),
    Vector2(500, 500)
]

for item in sorted(list_vectors):
    print(item)
# pos = Vector2(10, 25)
# dir = Vector2(0, 1)
# print(pos * dir)
# print(pos - dir)
# pos *= dir
# print(pos)
# pos -= dir
# print(pos)
