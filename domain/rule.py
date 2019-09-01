from domain.tile import HonorTile, SimpleTile, SimpleCategory


class RuleManager:
    @staticmethod
    def all_tiles():
        tiles = []
        for i in range(4):
            for category in [SimpleCategory.Dot, SimpleCategory.Bamboo, SimpleCategory.Character]:
                for number in range(1, 10):
                    tiles.append(SimpleTile(category, number))
            for name in ["east", "south", "west", "north", "red", "green", "white"]:
                tiles.append(HonorTile(name))
        return tiles
