from src.product import Product


def test_product_init(sample_product):
    assert sample_product.name == 'Raid'
    assert sample_product.description == 'Средство от комаров'
    assert sample_product.price == 400
    assert sample_product.quantity == 2


def test_new_product(product_dict):

    product = Product.new_product(product_dict)

    product.name = 'Samsung Galaxy C23 Ultra'
    product.description = '256GB, Серый цвет, 200MP камера'
    product.price = 180000.0
    product.quantity = 5


def test_price_update(capsys, sample_product):
    sample_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == 'Цена не должна быть нулевая или отрицательная.'

    sample_product.price = 250
    assert sample_product.price == 250


def test_product_str(sample_product):
    assert str(sample_product) == 'Raid, 400 руб. Остаток: 2 шт.'


def test_product_add(sample_a, sample_b):
    assert sample_a + sample_b == 3197.98
