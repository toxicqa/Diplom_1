import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize(
        "name",
        [
            "black bun",
            "white bun",
            "",
            "очень длинное название булочки с пробелами и символами !@#",
        ],
    )
    def test_get_name(self, name):
        price = 100
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize(
        "price",
        [100, 200.5, 0, -10],
    )
    def test_get_price(self, price):
        name = "black bun"
        bun = Bun(name, price)
        assert bun.get_price() == price
