"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_class_item_init(test_example):
    assert test_example.name == "Смартфон"
    assert test_example.price == 10000
    assert test_example.quantity == 20


def test_calculate_total_price(test_example):
    assert test_example.calculate_total_price() == 200000


def test_apply_discount(test_example):
    test_example.apply_discount()
    assert test_example.price == 8000


def test_name_setter(test_example):
    test_example.name = "Телефон"
    assert test_example.name == "Телефон"
    test_example.name = "Супер Телефон"
    assert test_example.name == "Супер Теле"


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr_str(test_example):
    assert repr(test_example) == "Item('Смартфон', 10000, 20)"
    assert str(test_example) == 'Смартфон'


def test_add(test_example, test_example2):
    assert test_example + test_example2 == 25
    assert test_example2 + test_example2 == 10