import pytest

from jongpy.domain.player import Player
from jongpy.domain.tile import hand_from_tenhou_string


class TestPlayer:
    @pytest.mark.parametrize(
        "s, res",
        [
            ("", 13),
            ("1p", 12),
            ("123456789p456s77m", 11),
            ("123456789p456s77z", 9),
            ("19p19s19m12345677z", -1),
        ],
    )
    def test_shanten_13orphans(self, s, res):
        player = Player()
        player.hand = hand_from_tenhou_string(s)
        assert player.shanten_13orphans() == res

    @pytest.mark.parametrize(
        "s, res",
        [
            ("", 6),
            ("11p", 5),
            ("123456789p456s77m", 5),
            ("11223344556678p", 0),
            ("11223344556677p", -1),
        ],
    )
    def test_shanten_7pairs(self, s, res):
        player = Player()
        player.hand = hand_from_tenhou_string(s)
        assert player.shanten_7pairs() == res

    @pytest.mark.parametrize(
        "s, res",
        [
            ("", 8),
            ("123p444s55m", 3),
            ("123456789p456s77m", -1),
            ("111222333444m55s", -1),
            ("123456m777888s9m", 0),
        ],
    )
    def test_shanten_basic(self, s, res):
        player = Player()
        player.hand = hand_from_tenhou_string(s)
        assert player.shanten_basic() == res
