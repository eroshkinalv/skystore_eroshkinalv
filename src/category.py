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
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, *args: Product):

        for product in args:
            self.__products.append(product)

        Category.product_count += len(args)

        return self.__products

    @property
    def products(self):

        prod_str = ''
        for product in self.__products:
            prod_str += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'

        return prod_str

    @property
    def products_list(self):
        return self.__products
