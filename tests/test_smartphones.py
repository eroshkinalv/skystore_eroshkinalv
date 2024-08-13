import pytest


def test_smartphones_init(smartphone_1):
    assert smartphone_1.name == "Iphone 15"
    assert smartphone_1.description == "512GB, Gray space"
    assert smartphone_1.price == 210000.0
    assert smartphone_1.quantity == 8
    assert smartphone_1.efficiency == 98.2
    assert smartphone_1.model == "15"
    assert smartphone_1.memory == 512
    assert smartphone_1.color == "Gray space"


def test_smartphones_add(smartphone_1, smartphone_2):
    assert smartphone_1 + smartphone_2 == 2114000.0


def test_smartphones_add_error(smartphone_1, lawn_grass_1):
    with pytest.raises(TypeError):
        assert smartphone_1 + lawn_grass_1
