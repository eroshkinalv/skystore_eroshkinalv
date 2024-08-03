from src.product import Product


class Category:
    """Класс с информацией по категориям товаров"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0


if __name__ == '__main__':
    product_1 = Product('Raid', 'Средство от комаров', 400, 333)
    product_2 = Product('Mosquitall', 'Средство от комаров', 359.99, 499)
    product_3 = Product('Раптор', 'Средство от комаров', 460, 564)

    category = Category('Хозяйственные товары', 'Против насекомых и грызунов', [product_1, product_2, product_3])

    print(category.name)
    print(category.description)
    print(category.products)
    print(category.category_count)
    print(category.product_count)
