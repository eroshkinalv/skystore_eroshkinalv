import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator


@pytest.fixture
def sample_product():
    return Product('Raid', 'Средство от комаров', 400, 2)


@pytest.fixture
def sample_a():
    return Product('TrueStyle', 'Футболка нарядная', 999, 2)


@pytest.fixture
def sample_b():
    return Product('Brands club', 'Футболка базовая', 599.99, 2)


@pytest.fixture
def category_a():
    return Category(
        name='Футболки',
        description='Футболки на все случаи жизни',
        products=[Product('NoName', 'Футболка оверсайз', 659, 1),
                  Product('Brands club', 'Футболка базовая', 599.99, 2),
                  Product('FakeNike', 'Футболка спортивная', 685, 3)]
    )


@pytest.fixture
def category_b():
    return Category(
        name='Наушники',
        description='Гарнитуры и наушники',
        products=[Product('Device', 'Беспроводные наушники', 1259, 1),
                  Product('XMi', 'Беспроводные наушники', 3599.99, 2),
                  Product('EarPod', 'Беспроводные наушники', 5685, 3)]
    )


@pytest.fixture
def add_product_category_a():
    return [Product('NoName', 'Футболка оверсайз', 659, 1),
            Product('Brands club', 'Футболка базовая', 599.99, 2),
            Product('FakeNike', 'Футболка спортивная', 685, 3)]


@pytest.fixture
def json_data():
    return [{"name": "Смартфоны",
            "description": "Смартфоны, как средство коммуникации",
             "products": [{
                 "name": "Samsung Galaxy C23 Ultra",
                 "description": "256GB, Серый цвет, 200MP камера",
                 "price": 180000.0,
                 "quantity": 5},
                 {"name": "Iphone 15",
                  "description": "512GB, Gray space",
                  "price": 210000.0,
                  "quantity": 8},
                 {"name": "Xiaomi Redmi Note 11",
                  "description": "1024GB, Синий",
                  "price": 31000.0,
                  "quantity": 14}]},
            {"name": "Телевизоры",
             "description": "Современный телевизор, который позволяет наслаждаться просмотром",
             "products": [{
                 "name": "55\" QLED 4K",
                 "description": "Фоновая подсветка",
                 "price": 123000.0,
                 "quantity": 7}]}]


@pytest.fixture
def product_dict():
    return {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5}


@pytest.fixture
def product_iterator(category_a):
    return ProductIterator(category_a)
