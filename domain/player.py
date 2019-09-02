from functools import reduce
from typing import List

from domain.table import Table
from domain.tile import (HonorCategory, HonorTile, SimpleCategory, SimpleTile,
                         Tile)


class Player:
    def __init__(self):
        self.table = Table()
        # initialize hand
        self.hand = {}
        for category in SimpleCategory:
            self.hand[category] = [0] * 9
        self.hand[HonorCategory.Wind] = [0] * 4
        self.hand[HonorCategory.Dragon] = [0] * 3

    def draw_tiles(self, num: int) -> None:
        for tile in self.table.discharge_tiles(num):
            if tile.category in SimpleCategory:
                self.hand[tile.category][int(tile.number) - 1] += 1
            elif tile.category == HonorCategory.Wind:
                d = {"east": 0, "south": 1, "west": 2, "north": 3}
                self.hand[tile.category][d[tile.number]] += 1
            elif tile.category == HonorCategory.Dragon:
                d = {"red": 0, "green": 1, "white": 2}
                self.hand[tile.category][d[tile.number]] += 1

    def hand_to_list(self) -> List[Tile]:
        res = []
        wind_dict = {0: "east", 1: "south", 2: "west", 3: "north"}
        dragon_dict = {0: "red", 1: "green", 2: "white"}
        for cat, counts in self.hand.items():
            for no, count in enumerate(counts):
                for _ in range(count):
                    if type(cat) == SimpleCategory:
                        res.append(SimpleTile(cat, no + 1))
                    elif cat == HonorCategory.Wind:
                        res.append(HonorTile(wind_dict[no]))
                    elif cat == HonorCategory.Dragon:
                        res.append(HonorTile(dragon_dict[no]))
        return res

    def hand_to_string(self):
        return reduce(lambda a, b: a + str(b), self.hand_to_list(), "")

    def hand_to_color_string(self):
        return reduce(lambda a, b: a + b.color_string(), self.hand_to_list(), "")
