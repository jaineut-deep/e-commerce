from typing import Iterator

from src.category import Category
from src.product import Product


class GoodsIter:
    """Класс для реализации перебора продуктов из объекта класса Category."""

    data_category: Category
    index_count: int

    def __init__(self, data_category: Category):
        self.data_category = data_category
        self.index_count = 0

    def __iter__(self) -> Iterator:
        """Магический метод, который возвращает итератор объекта класса Category."""

        self.index_count = 0
        return self

    def __next__(self) -> Product:
        """Магический метод, возвращающий следующий элемент последовательности объекта класса Category."""

        if self.index_count < len(self.data_category.category_products):
            product_entity = self.data_category.category_products[self.index_count]
            self.index_count += 1
            return product_entity
        else:
            raise StopIteration
