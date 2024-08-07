import pytest


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == 'NoName'
    assert next(product_iterator).name == 'Brands club'
    assert next(product_iterator).name == 'FakeNike'

    with pytest.raises(StopIteration):
        next(product_iterator)
