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

    def __str__(self):
        return f'{self.name}, количество продуктов: {sum([pr.quantity for pr in self.__products])} шт.'

    def add_product(self, *args: Product):

        for product in args:
            if isinstance(product, Product):
                self.__products.append(product)
            else:
                raise TypeError

        Category.product_count += len(args)

        return self.__products

    @property
    def products(self):

        prod_str = ''
        for product in self.__products:
            prod_str += f'{str(product)}\n'

        return prod_str

    @property
    def products_list(self):
        return self.__products

    def middle_price(self):

        try:
            return round(sum([prod.price for prod in self.__products]) / len(self.__products), 2)

        except ZeroDivisionError:
            return 0
