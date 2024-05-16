
from praktikum.bun import Bun


class TestBun:

    def test_bun_get_name(self):
        bun = Bun('black bun', 100)
        assert bun.name == 'black bun', "Некорректное название булки"

    def test_bun_get_price(self):
        bun = Bun('white bun', 200)
        assert bun.price == 200, "Некорректная стоимость булки"
