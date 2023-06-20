"""Здесь надо написать тесты с использованием pytest для модуля item."""
def test_class_item(test_example):
    assert test_example.name == "Смартфон"
    assert test_example.price == 10000
    assert test_example.quantity == 20
    assert test_example.calculate_total_price() == 200000
    test_example.apply_discount()
    assert test_example.price == 8000
