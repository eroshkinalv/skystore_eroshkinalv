import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone


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


@pytest.fixture
def smartphone_1():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def smartphone_2():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def lawn_grass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawn_grass_2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
