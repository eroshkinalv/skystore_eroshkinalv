import os
from unittest.mock import patch

from src.utils import create_objects_from_json, get_json_data


@patch('json.load')
def test_get_json_data(mock_json, json_data):
    mock_json.return_value = json_data
    assert get_json_data(os.path.abspath(r'..\data\products.json')) == json_data


def test_create_objects_from_json(json_data):
    result = create_objects_from_json(json_data)
    assert result[0].name == 'Смартфоны'
    assert result[0].description == 'Смартфоны, как средство коммуникации'
    assert len(result[0].products_list) == 3
