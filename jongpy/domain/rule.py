from itertools import chain

from jongpy.domain.player import Player
from jongpy.domain.tile import HonorCategory, HonorTile, SimpleCategory, SimpleTile


class RuleManager:
    @staticmethod
    def all_tiles():
        tiles = []
        for i in range(4):
            for category in [
                SimpleCategory.Dot,
                SimpleCategory.Bamboo,
                SimpleCategory.Character,
            ]:
                for number in range(1, 10):
                    tiles.append(SimpleTile(category, number))
            for name in ["east", "south", "west", "north", "red", "green", "white"]:
                tiles.append(HonorTile(name))
        return tiles


class Yaku:
    @staticmethod
    def is_13orphans(player: Player) -> bool:
        """ 国士無双 """
        # FIXME: double limit
        return player.shanten_13orphans() == -1

    @staticmethod
    def is_4concealed_triplets(player: Player) -> bool:
        """ 四暗刻 """
        li = [i for i in chain.from_iterable(player.hand.values()) if i == 3 or i == 2]
        return (
            len([i for i in li if i == 3]) == 4 and len([i for i in li if i == 2]) == 1
        )

    @staticmethod
    def is_big_3dragons(player: Player) -> bool:
        """ 大三元 """
        return player.shanten_basic() == -1 and all(
            i == 3 for i in player.hand[HonorCategory.Dragon]
        )

    @staticmethod
    def is_little_4winds(player: Player) -> bool:
        """ 小四喜 """
        return (
            player.shanten_basic() == -1
            and len([i for i in player.hand[HonorCategory.Wind] if i == 3]) == 3
            and len([i for i in player.hand[HonorCategory.Wind] if i == 2]) == 1
        )

    @staticmethod
    def is_big_4winds(player: Player) -> bool:
        """ 大四喜 """
        return player.shanten_basic() == -1 and all(
            i == 3 for i in player.hand[HonorCategory.Wind]
        )

    @staticmethod
    def is_all_honors(player: Player) -> bool:
        """ 清一色 """
        return player.shanten_basic() == -1 and all(
            i == 3 or i == 2
            for i in chain(
                player.hand[HonorCategory.Wind], player.hand[HonorCategory.Dragon]
            )
        )

    @staticmethod
    def is_all_terminals(player: Player) -> bool:
        """ 清老頭 """
        if player.shanten_basic() != -1:
            return False
        for category in SimpleCategory:
            if not all(i in [2, 3] for i in player.hand[category][0::8]):
                return False
        return True

    @staticmethod
    def is_all_green(player: Player) -> bool:
        """ 緑一色 """
        if player.shanten_basic() != -1:
            return False
        li = [player.hand[HonorCategory.Dragon][1]]
        for i in [2, 3, 4, 6, 8]:
            li.append(player.hand[SimpleCategory.Bamboo][i])
        return sum(li) == 14

    @staticmethod
    def is_9gates(player: Player) -> bool:
        # FIXME: double limit
        if player.shanten_basic() != -1:
            return False
        for category in SimpleCategory:
            if (
                player.hand[category][0] == 3
                and player.hand[category][-1] == 3
                and all(i in [1, 2] for i in player.hand[category][1:-1])
            ):
                return True
        return False

    # TODO: limit hands
    # - 4kans
    # - heavenly hand
    # - hand of earth
    # - hand of man

    @staticmethod
    def is_7pairs(player: Player) -> bool:
        """ 七対子 """
        return player.shanten_7pairs() == -1
