import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def test_example():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    return item1

@pytest.fixture
def test_example2():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    return phone1
