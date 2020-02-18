from bll import GameCoreController


class GameConsoleView:
    def __init__(self):
        self.__controller = GameCoreController()

    def print_list(self):
        for item in self.__controller.map:
            for i in item:
                print(i, end="\t")
            print()

    def main(self):
        self.__controller.generate_new_number()
        self.__controller.generate_new_number()
        self.print_list()
        while True:
            self.display_options()
            self.update()

    def display_options(self):
        print(""""A"向左，"D"向右，"W"向上，"S"向下""")

    def move_map_input(self):
        str_input = input("请输入选项：")
        if str_input == "A":
            self.__controller.move_left()
        elif str_input == "D":
            self.__controller.move_right()
        elif str_input == "W":
            self.__controller.move_up()
        elif str_input == "S":
            self.__controller.move_down()

    def update(self):
        self.move_map_input()
        self.__controller.generate_new_number()
        self.print_list()
        if self.__controller.is_game_over():
            print("游戏结束")
