from domain.rule import RuleManager
import random


class Table:
    def __init__(self):
        self.tiles_in_wall = []
        self.reset_tiles_in_wall()

    def reset_tiles_in_wall(self):
        self.tiles_in_wall = RuleManager.all_tiles()

    def discharge_tiles(self, num):
        if len(self.tiles_in_wall) >= num:
            chosen_tiles = random.sample(self.tiles_in_wall, num)
            for tile in chosen_tiles:
                self.tiles_in_wall.remove(tile)
            return chosen_tiles
        else:
            return []
