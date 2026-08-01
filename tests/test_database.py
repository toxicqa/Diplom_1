from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_available_buns_count(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3

    def test_available_buns_content(self):
        db = Database()
        buns = db.available_buns()
        names = [bun.get_name() for bun in buns]
        prices = [bun.get_price() for bun in buns]
        assert names == ["black bun", "white bun", "red bun"]
        assert prices == [100, 200, 300]

    def test_available_ingredients_count(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    def test_available_ingredients_types_and_content(self):
        db = Database()
        ingredients = db.available_ingredients()
        types = [ing.get_type() for ing in ingredients]
        names = [ing.get_name() for ing in ingredients]
        prices = [ing.get_price() for ing in ingredients]

        assert types.count(INGREDIENT_TYPE_SAUCE) == 3
        assert types.count(INGREDIENT_TYPE_FILLING) == 3
        assert names == ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]
        assert prices == [100, 200, 300, 100, 200, 300]
