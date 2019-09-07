import inspect

import pytest

from jongpy.domain.tile import HonorCategory, SimpleCategory, hand_from_tenhou_string

empty_hand = {
    SimpleCategory.Dot: [0] * 9,
    SimpleCategory.Bamboo: [0] * 9,
    SimpleCategory.Character: [0] * 9,
    HonorCategory.Wind: [0] * 4,
    HonorCategory.Dragon: [0] * 3,
}


@pytest.mark.parametrize(
    "s, res",
    [
        (
            "11122233344455p",
            {**empty_hand, SimpleCategory.Dot: [3, 3, 3, 3, 2, 0, 0, 0, 0]},
        ),
        (
            "123p456s789m12345z",
            {
                **empty_hand,
                SimpleCategory.Dot: [1, 1, 1, 0, 0, 0, 0, 0, 0],
                SimpleCategory.Bamboo: [0, 0, 0, 1, 1, 1, 0, 0, 0],
                SimpleCategory.Character: [0, 0, 0, 0, 0, 0, 1, 1, 1],
                HonorCategory.Wind: [1, 1, 1, 1],
                HonorCategory.Dragon: [1, 0, 0],
            },
        ),
        ("1", AttributeError),
        ("p", AttributeError),
        ("foo", AttributeError),
        ("1p9", AttributeError),
    ],
)
def test_hand_from_tenhou_string(s, res):
    if inspect.isclass(res) and issubclass(res, BaseException):
        with pytest.raises(res):
            hand_from_tenhou_string(s)
    else:
        assert hand_from_tenhou_string(s) == res
