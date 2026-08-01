import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize(
        "name, price",
        [
            ("black bun", 100),
            ("white bun", 200.5),
            ("", 0),
            ("очень длинное название булочки с пробелами и символами !@#", 9999.99),
        ],
    )
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize(
        "name, price",
        [
            ("black bun", 100),
            ("white bun", 200.5),
            ("red bun", 0),
            ("test", -10),
        ],
    )
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
