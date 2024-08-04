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
