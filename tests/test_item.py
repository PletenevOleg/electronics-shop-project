"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def test_product():
    return Item("Планшет", 12000, 10)


def test_init(test_product):
    assert test_product.name == "Планшет"
    assert test_product.price == 12000
    assert test_product.quantity == 10


def test_calculate_total_price(test_product):
    assert test_product.calculate_total_price() == 120000


def test_apply_discount(test_product):
    test_product.apply_discount()
    assert test_product.price == 12000.0
    test_product.pay_rate = 0.5
    test_product.apply_discount()
    assert test_product.price == 6000.0


def test_all(test_product):
    assert Item.all != []


def test_name(test_product):
    assert test_product.name == 'Планшет'
    test_product.name = 'Пылесос'
    assert test_product.name == 'Пылесос'
    with pytest.raises(Exception):
        test_product.name = "РоботПылесос"


def test_instantiate_from_csv(test_product):
    test_product.instantiate_from_csv()
    assert len(test_product.all) == 5


def test_string_to_number():
    assert Item.string_to_number('3.6') == 3


def test_repr(test_product):
    assert test_product.__repr__() == "Item('Планшет', 12000, 10)"


def test_str(test_product):
    assert test_product.__str__() == 'Планшет'
