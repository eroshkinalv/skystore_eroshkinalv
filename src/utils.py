import json
import os
from typing import Dict

from src.category import Category
from src.product import Product


def get_json_data(path: str) -> Dict:

    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    return json_data


def create_objects_from_json(data: Dict) -> list:

    products = []

    for product in data:
        prod_list = []
        for pr in product['products']:
            prod_list.append(Product(**pr))
        product['products'] = prod_list

        products.append(Category(**product))

    return products


if __name__ == '__main__':
    raw_data = get_json_data(r'..\data\products.json')
    product_data = create_objects_from_json(raw_data)
    print(product_data[0].name)
    print(product_data[0].description)
    print(product_data[0].products_list)
    print(product_data)
