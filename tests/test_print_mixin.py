from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixins(capsys):
    Product('Raid', 'Средство от комаров', 400, 2)
    message = capsys.readouterr()
    assert message.out.strip() == 'Product (Raid, Средство от комаров, 400, 2)'

    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    message = capsys.readouterr()
    assert message.out.strip() == 'Smartphone (Iphone 15, 512GB, Gray space, 210000.0, 8)'

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == 'LawnGrass (Газонная трава, Элитная трава для газона, 500.0, 20)'
