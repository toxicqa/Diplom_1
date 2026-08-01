import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ing1 = Mock()
        mock_ing2 = Mock()
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ing2

    def test_move_ingredient(self):
        burger = Burger()
        mock_ing1 = Mock()
        mock_ing2 = Mock()
        mock_ing3 = Mock()
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)
        burger.add_ingredient(mock_ing3)
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [mock_ing2, mock_ing3, mock_ing1]

    def test_get_price_only_bun(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        assert burger.get_price() == 200  # 2 * bun price

    def test_get_price_with_ingredients(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)

        mock_ing1 = Mock()
        mock_ing1.get_price.return_value = 50
        mock_ing2 = Mock()
        mock_ing2.get_price.return_value = 75
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)

        assert burger.get_price() == 325  # 200 + 50 + 75

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)

        mock_ing = Mock()
        mock_ing.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ing.get_name.return_value = "hot sauce"
        mock_ing.get_price.return_value = 100
        burger.add_ingredient(mock_ing)

        receipt = burger.get_receipt()
        expected = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 300"
        )
        assert receipt == expected

    @pytest.mark.parametrize(
        "bun_price, ingredients_prices, expected_price",
        [
            (100, [], 200),
            (150, [50], 350),
            (100, [100, 200, 50], 550),
            (0, [10, 20], 30),
        ],
    )
    def test_get_price_parametrized(self, bun_price, ingredients_prices, expected_price):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ingredients_prices:
            mock_ing = Mock()
            mock_ing.get_price.return_value = price
            burger.add_ingredient(mock_ing)

        assert burger.get_price() == expected_price
