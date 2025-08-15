from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс с основной информацией по товарам"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):

        self.name = name
        self.description = description
        self.__price = price

        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError('Товар с нулевым количеством не может быть добавлен.')

        super().__init__()

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):

        if type(other) is Product:
            return (self.__price * self.quantity) + (other.price * other.quantity)

        raise TypeError

    @classmethod
    def new_product(cls, prod_data: dict):
        return cls(**prod_data)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная.")
            return
        else:
            self.__price = new_price
