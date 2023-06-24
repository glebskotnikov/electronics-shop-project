import pytest

from src.item import Item


@pytest.fixture
def test_example():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    return item1
