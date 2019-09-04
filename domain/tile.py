from enum import Enum
from typing import Dict, List

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

    @staticmethod
    def wind_values():
        return ["east", "south", "west", "north"]

    @staticmethod
    def dragon_values():
        return ["red", "green", "white"]


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
        if name in HonorCategory.wind_values():
            super().__init__(HonorCategory.Wind, name)
        elif name in HonorCategory.dragon_values():
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


def hand_from_tenhou_string(s: str) -> Dict[Category, List[int]]:
    res = {
        SimpleCategory.Dot: [0] * 9,
        SimpleCategory.Bamboo: [0] * 9,
        SimpleCategory.Character: [0] * 9,
        HonorCategory.Wind: [0] * 4,
        HonorCategory.Dragon: [0] * 3,
    }
    buf = []
    for c in s:
        # 0 means red 5. treat 0 as 5
        if c in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            buf.append(int(c))
        elif c in ["p", "s", "m"]:
            if len(buf) == 0:
                raise AttributeError(f"failed to parse string: {s}")
            d = {
                "p": SimpleCategory.Dot,
                "s": SimpleCategory.Bamboo,
                "m": SimpleCategory.Character,
            }
            for num in buf:
                if num == 0:
                    num = 5
                res[d[c]][num - 1] += 1
            buf = []
        elif c == "z":
            if len(buf) == 0:
                raise AttributeError(f"failed to parse string: {s}")
            for num in buf:
                if num - 4 <= 0:
                    res[HonorCategory.Wind][num - 1] += 1
                elif 1 <= num - 4 <= 3:
                    res[HonorCategory.Dragon][num - 5] += 1
                else:
                    raise AttributeError(f"failed to parse string: {s}")
            buf = []
        else:
            raise AttributeError(f"failed to parse string: {s}")
    if len(buf) > 0:
        raise AttributeError(f"failed to parse string: {s}")
    return res
