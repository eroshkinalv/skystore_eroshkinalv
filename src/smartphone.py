from src.product import Product


class Smartphone(Product):
    """Класс-наследник от исходного класса Product.
        Содержит информацию по товарам относящимся к категории "Смартфоны"."""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):

        if type(other) is Smartphone:
            return (self.price * self.quantity) + (other.price * other.quantity)

        raise TypeError