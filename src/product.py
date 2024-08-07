class Product:
    """Класс с основной информацией по товарам"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        return (self.__price * self.quantity) + (other.price * other.quantity)

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
