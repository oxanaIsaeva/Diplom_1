from random import choice
from unittest.mock import Mock

import pytest

from praktikum.burger import Burger
from praktikum.database import Database


class TestBurger:

    @pytest.mark.parametrize(
        'name, price',
        [
            ['black bun', 100],
            ['white bun', 200],
            ['red bun', 300]
        ]
    )
    def test_set_buns(self, name, price):
        mock_bun = Mock()
        mock_bun.get_name.return_value = name
        mock_bun.get_price.return_value = price

        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun, "Бургер состоит из неправильных булок"

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
    def test_add_ingredient(self, ing_type, name, price):
        mock_ingredient = Mock()
        mock_ingredient.type = ing_type
        mock_ingredient.name = name
        mock_ingredient.price = price

        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert mock_ingredient in burger.ingredients, "Бургер состоит из неправильных ингредиентов"

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
    def test_remove_ingredient(self, ing_type, name, price):
        mock_ingredient = Mock()
        mock_ingredient.type = ing_type
        mock_ingredient.name = name
        mock_ingredient.price = price

        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == [], "Не удалось удалить ингредиент"

    def test_move_ingredient(self):
        mock_ingredient = Mock()
        mock_ingredient.type = 'SAUCE'
        mock_ingredient.name = 'hot sauce'
        mock_ingredient.price = 100.0

        mock_ingredient_cutlet = Mock()
        mock_ingredient_cutlet.type = 'FILLING'
        mock_ingredient_cutlet.name = 'cutlet'
        mock_ingredient_cutlet.price = 100.0

        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient_cutlet)
        burger.move_ingredient(1, 0)

        assert burger.ingredients == [mock_ingredient_cutlet, mock_ingredient], "Не удалось переместить ингредиент"

    def test_get_price(self):
        burger = Burger()
        database = Database()
        buns = database.available_buns()
        bun = choice(buns)
        ingredients = database.available_ingredients()
        ingredient = choice(ingredients)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        assert burger.get_price() == bun.get_price() * 2 + ingredient.get_price(), 'Некорректная стоимость бургера'

    def test_get_receipt(self):
        burger = Burger()
        database = Database()
        buns = database.available_buns()
        bun = buns[1]
        ingredients = database.available_ingredients()
        ingredient_sauce = ingredients[2]
        ingredient_sausage = ingredients[5]
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_sausage)

        assert burger.get_receipt() == ('(==== white bun ====)\n= sauce chili sauce =\n= filling sausage =\n'
                                        '(==== white bun ====)\n\nPrice: 1000'), 'Некорректный рецепт бургера'
