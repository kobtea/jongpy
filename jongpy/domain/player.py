from functools import reduce
from typing import List

from jongpy.domain.table import Table
from jongpy.domain.tile import (
    HonorCategory,
    HonorTile,
    SimpleCategory,
    SimpleTile,
    Tile,
)


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
                d = dict([(v, k) for k, v in enumerate(HonorCategory.wind_values())])
                self.hand[tile.category][d[tile.number]] += 1
            elif tile.category == HonorCategory.Dragon:
                d = dict([(v, k) for k, v in enumerate(HonorCategory.dragon_values())])
                self.hand[tile.category][d[tile.number]] += 1

    def hand_to_list(self) -> List[Tile]:
        res = []
        wind_dict = dict(enumerate(HonorCategory.wind_values()))
        dragon_dict = dict(enumerate(HonorCategory.dragon_values()))
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

    def shanten_13orphans(self) -> int:
        """
        calculate shanten for thirteen orphans (国士無双)
        :return: int
        """
        res = 13
        available_counts = []
        for category, counts in self.hand.items():
            if category in SimpleCategory:
                available_counts.append(counts[0])
                available_counts.append(counts[-1])
            elif category in HonorCategory:
                available_counts += counts
        res -= len([i for i in available_counts if i >= 1])
        if any([i == 2 for i in available_counts]):
            res -= 1
        return res

    def shanten_7pairs(self) -> int:
        """
        calculate shanten for seven pairs (七対子)
        :return: int
        """
        res = 6
        for counts in self.hand.values():
            res -= len([i for i in counts if i == 2])
        return res
