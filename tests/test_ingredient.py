import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize(
        "ingredient_type",
        [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING],
    )
    def test_get_type(self, ingredient_type):
        name = "hot sauce"
        price = 100
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize(
        "name",
        ["hot sauce", "", "очень длинное название ингредиента с пробелами и символами !@#"],
    )
    def test_get_name(self, name):
        ingredient_type = INGREDIENT_TYPE_SAUCE
        price = 100
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize(
        "price",
        [100, 0, 200.75, -10],
    )
    def test_get_price(self, price):
        ingredient_type = INGREDIENT_TYPE_SAUCE
        name = "hot sauce"
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price
