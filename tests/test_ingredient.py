import pytest

from praktikum.ingredient import Ingredient


class TestIngredient:

    @pytest.mark.parametrize(
        'ing_type, name, price',
        [
            ['SAUCE', 'hot sauce', 100],
            ['SAUCE', 'sour cream', 200],
            ['SAUCE', 'chili sauce', 300],
            ['FILLING', 'cutlet', 100],
            ['FILLING', 'dinosaur', 200],
            ['FILLING', 'sausage', 300]
        ]
    )
    def test_ingredient_get_type(self, ing_type, name, price):
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.type == ing_type, "Некорректный тип ингредиента"

    @pytest.mark.parametrize(
        'ing_type, name, price',
        [
            ['SAUCE', 'hot sauce', 100],
            ['SAUCE', 'sour cream', 200],
            ['SAUCE', 'chili sauce', 300],
            ['FILLING', 'cutlet', 100],
            ['FILLING', 'dinosaur', 200],
            ['FILLING', 'sausage', 300]
        ]
    )
    def test_ingredient_get_name(self, ing_type, name, price):
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.name == name, "Некорректное имя ингредиента"

    @pytest.mark.parametrize(
        'ing_type, name, price',
        [
            ['SAUCE', 'hot sauce', 100],
            ['SAUCE', 'sour cream', 200],
            ['SAUCE', 'chili sauce', 300],
            ['FILLING', 'cutlet', 100],
            ['FILLING', 'dinosaur', 200],
            ['FILLING', 'sausage', 300]
        ]
    )
    def test_ingredient_get_price(self, ing_type, name, price):
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.price == price, "Некорректная стоимость ингредиента"
