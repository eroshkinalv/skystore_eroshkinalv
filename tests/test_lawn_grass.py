import pytest


def test_lawn_grass_init(lawn_grass_1):
    assert lawn_grass_1.name == "Газонная трава"
    assert lawn_grass_1.description == "Элитная трава для газона"
    assert lawn_grass_1.price == 500.0
    assert lawn_grass_1.quantity == 20
    assert lawn_grass_1.country == "Россия"
    assert lawn_grass_1.germination_period == "7 дней"
    assert lawn_grass_1.color == "Зеленый"


def test_lawn_grass_add(lawn_grass_1, lawn_grass_2):
    assert lawn_grass_1 + lawn_grass_2 == 16750


def test_lawn_grass_add_error(lawn_grass_1, sample_product):
    with pytest.raises(TypeError):
        assert lawn_grass_1 + sample_product
