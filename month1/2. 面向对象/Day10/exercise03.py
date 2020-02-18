class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def up():
        return Vector2(-1, 0)

    @staticmethod
    def left():
        return Vector2(0, -1)


pos = Vector2(1, 1)

# left=Vector2.left()
# pos.x+=left.x
# pos.y+=left.y
#
# print(pos.x,pos.y)

up = Vector2.up()
pos.x += up.x
pos.y += up.y
print(pos.x, pos.y)
