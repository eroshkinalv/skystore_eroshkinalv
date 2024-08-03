def test_category_init(category_a, category_b):
    assert category_a.name == 'Футболки'
    assert category_a.description == 'Футболки на все случаи жизни'
    assert len(category_a.products) == 3

    assert category_a.category_count == 2
    assert category_b.category_count == 2

    assert category_a.product_count == 6
    assert category_b.product_count == 6
