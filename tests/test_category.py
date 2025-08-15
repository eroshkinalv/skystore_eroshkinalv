import pytest


def test_category_init(category_a, category_b):
    assert category_a.name == 'Футболки'
    assert category_a.description == 'Футболки на все случаи жизни'
    assert len(category_a.products_list) == 3

    assert category_a.category_count == 2
    assert category_b.category_count == 2

    assert category_a.product_count == 6
    assert category_b.product_count == 6


def test_category_add_product(category_a):
    assert category_a.products == ('NoName, 659 руб. Остаток: 1 шт.\nBrands club, 599.99 руб. Остаток: 2 шт.\n'
                                   'FakeNike, 685 руб. Остаток: 3 шт.\n')


def test_category_str(category_a):
    assert str(category_a) == 'Футболки, количество продуктов: 6 шт.'


def test_category_add_product_error(category_a):
    with pytest.raises(TypeError):
        assert category_a.add_product("Not a product")


def test_middle_price(category_a, no_products_in_category):
    assert category_a.middle_price() == 648.00
    assert no_products_in_category.middle_price() == 0
