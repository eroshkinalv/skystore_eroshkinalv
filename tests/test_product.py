def test_product_init(sample_product):
    assert sample_product.name == 'Raid'
    assert sample_product.description == 'Средство от комаров'
    assert sample_product.price == 400
    assert sample_product.quantity == 2
