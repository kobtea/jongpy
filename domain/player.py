from functools import reduce

from domain.table import Table


class Player:
    def __init__(self):
        self.table = Table()
        self.hand = []

    def draw_tiles(self, num: int):
        self.hand += self.table.discharge_tiles(num)

    def hand_to_string(self):
        return reduce(lambda a, b: a + str(b), self.hand, "")

    def hand_to_color_string(self):
        return reduce(lambda a, b: a + b.color_string(), self.hand, "")
