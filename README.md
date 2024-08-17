# Проект skystore_eroshkinalv

## Описание:

Проект skystore_eroshkinalv - это учебный проект на Python, который представляет собой ядро для интернет-магазина c использованием классов и объектов на основе популярной темы e-commerce. 
В дальнейшем для этого ядра возможно будет реализовать любой интерфейс — от сайта до телеграм-бота.
(На данном этапе реализации отсутствует система платежей)

- Для классов Product и Category добавлен класс-метод для создания нового товара, а также реализованы геттер и сеттер для цены товара. Изменены режимы доступа для атрибутов price и products на приватные.
- Для класса Product добавлено строковое отображение (Название продукта, 80 руб. Остаток: 15 шт.)
- Для класса Category добавлено строковое отображение (Название категории, количество продуктов: 200 шт.)
- Для удобства работы с продуктами реализована возможность их складывать.
- Создан вспомогательный класс, ProductIterator, с помощью которого можно перебирать товары одной категории.
- Созданы классы Smartphone и LawnGrass, которые являются классами-наследниками от исходного класса Product.
- Доработан функционал сложения таким образом, чтобы можно было складывать товары только из одинаковых классов продуктов (в противном случае возникнет ошибка TypeError).
- Доработан метод, который добавляет продукт в категорию, таким образом, чтобы не было возможности добавить вместо продукта или его наследников любой другой объект.
- Создан базовый абстрактный класс с именем BaseProduct, который станет родительским для класса продуктов.
- Реализован класс-миксин, который будет при создании объекта, печатать в консоль информацию о том, от какого класса и с какими параметрами был создан объект.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/eroshkinalv/skystore_eroshkinalv.git
```

## Документация:

Для получения дополнительной информации обратитесь к [папки с документацией пока нет](README.md).

## Лицензия:

Этот проект лицензирован по [лицензии](LICENSE.txt).

## Тестирование:

Данный проект покрыт юнит-тестами. Для их запуска выполните команду:
```
pytest
```

