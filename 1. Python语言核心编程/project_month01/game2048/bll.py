import random
from model import Location


class GameCoreController:
    def __init__(self):
        self.__list_merge = None
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.__list_empty_location = []

    @property
    def map(self):
        return self.__map

    def __zero_to_end(self):
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def move_left(self):
        for line in self.__map:
            self.__list_merge = line
            self.__merge()

    def move_right(self):
        for line in self.__map:
            self.__list_merge = line[::-1]
            self.__merge()
            line[::-1] = self.__list_merge

    def __square_matrix_transpose(self):
        for c in range(len(self.__map) - 1):
            for r in range(c + 1, len(self.__map)):
                self.__map[r][c], self.__map[c][r] = self.__map[c][r], self.__map[r][c]

    def move_up(self):
        self.__square_matrix_transpose()
        self.move_left()
        self.__square_matrix_transpose()

    def move_down(self):
        self.__square_matrix_transpose()
        self.move_right()
        self.__square_matrix_transpose()

    def generate_new_number(self):
        self.__calculate_empty_location()
        if len(self.__list_empty_location) == 0:
            return
        loc = random.choice(self.__list_empty_location)
        self.__map[loc.r][loc.c] = self.__create_random_number()
        self.__list_empty_location.remove(loc)

    def __create_random_number(self):
        return 4 if random.randint(1, 10) == 1 else 2

    def __calculate_empty_location(self):
        self.__list_empty_location.clear()
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                if self.__map[r][c] == 0:
                    self.__list_empty_location.append(Location(r, c))

    def is_game_over(self):
        if len(self.__list_empty_location) > 0:
            return False
        for r in range(len(self.__map)):
            for c in range(len(self.__map) - 1):
                if self.__map[r][c] == self.__map[r][c + 1] or self.__map[c][r] == self.__map[c + 1][r]:
                    return False
        return True
