import pytest

from src.item import Item
from src.keyboard import Keyboard
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

@pytest.fixture
def test_example3():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    return kb
