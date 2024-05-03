import pytest

from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize(
        'name, price',
        [
            ['black bun', 100],
            ['white bun', 200],
            ['red bun', 300]
        ]
    )
    def test_bun_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name, "Некорректное название булки"

    @pytest.mark.parametrize(
        'name, price',
        [
            ['black bun', 100],
            ['white bun', 200],
            ['red bun', 300]
        ]
    )
    def test_bun_get_price1(self, name, price):
        bun = Bun(name, price)
        assert bun.price == price, "Некорректная стоимость булки"
