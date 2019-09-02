from enum import Enum

import colorama

colorama.init()


class Category(Enum):
    pass


class SimpleCategory(Category):
    Dot = "筒"
    Bamboo = "索"
    Character = "萬"

    def __str__(self):
        return self.value


class HonorCategory(Category):
    Wind = "風"
    Dragon = "字"

    def __str__(self):
        return self.value


class Tile:
    def __init__(self, category: Category, number: str):
        self.category = category
        self.number = number

    def __str__(self):
        return f"[{self.category}{self.number}]"

    def color_string(self):
        return self.__str__()


class SimpleTile(Tile):
    def __init__(self, category: SimpleCategory, number: int):
        if number in range(1, 10):
            super().__init__(category, str(number))
        else:
            raise AttributeError(f"invalid number for simple tile: {number}")

    def color_string(self):
        if self.category == SimpleCategory.Dot:
            return colorama.Back.BLUE + self.__str__() + colorama.Style.RESET_ALL
        elif self.category == SimpleCategory.Bamboo:
            return colorama.Back.GREEN + self.__str__() + colorama.Style.RESET_ALL
        else:
            return colorama.Back.MAGENTA + self.__str__() + colorama.Style.RESET_ALL


class HonorTile(Tile):
    def __init__(self, name: str):
        if name in ["east", "south", "west", "north"]:
            super().__init__(HonorCategory.Wind, name)
        elif name in ["red", "green", "white"]:
            super().__init__(HonorCategory.Dragon, name)
        else:
            raise AttributeError(f"invalid name for honor tile: {name}")

    def __str__(self):
        if self.category == HonorCategory.Wind and self.number == "east":
            return "[東 ]"
        elif self.category == HonorCategory.Wind and self.number == "south":
            return "[南 ]"
        elif self.category == HonorCategory.Wind and self.number == "west":
            return "[西 ]"
        elif self.category == HonorCategory.Wind and self.number == "north":
            return "[北 ]"
        elif self.category == HonorCategory.Dragon and self.number == "red":
            return "[中 ]"
        elif self.category == HonorCategory.Dragon and self.number == "green":
            return "[發 ]"
        elif self.category == HonorCategory.Dragon and self.number == "white":
            return "[白 ]"
        else:
            raise AttributeError(f"invalid honor tile: {self.category},{self.number}")

    def color_string(self):
        if self.category == HonorCategory.Wind:
            return colorama.Back.YELLOW + self.__str__() + colorama.Style.RESET_ALL
        else:
            return colorama.Back.CYAN + self.__str__() + colorama.Style.RESET_ALL
